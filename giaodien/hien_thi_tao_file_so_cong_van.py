import os
from pathlib import Path
import pandas as pd
import streamlit as st
from modules.office import join_xlsx_to_csv  # Import hàm join_xlsx_to_csv từ thư viện dung_lib

class HienThiFileSoCongVan:
    """
    Lớp để xử lý việc cập nhật số công văn từ các file Excel và hiển thị kết quả.
    """

    def __init__(self, directory: str, output_csv: str):
        """
        Khởi tạo đối tượng với đường dẫn thư mục chứa các file Excel và file CSV đầu ra.
        :param directory: Đường dẫn đến thư mục chứa các file Excel.
        :param output_csv: Đường dẫn đến file CSV đầu ra.
        """
        self.directory = directory
        self.output_csv = output_csv

    def cap_nhat_so_cong_van(self):
        """
        Cập nhật số công văn từ các file Excel trong thư mục và lưu kết quả vào file CSV.
        """
        try:
            df_combined = join_xlsx_to_csv(self.directory, self.output_csv)
            if df_combined is not None:
                st.success("Cập nhật và lưu số công văn thành công.")
            else:
                st.error("Có lỗi xảy ra khi cập nhật số công văn.")
        except Exception as e:
            st.error(f"Đã xảy ra lỗi: {e}")

    def hien_thi_so_cong_van(self):
        """
        Hiển thị nội dung file CSV số công văn.
        """
        try:
            if os.path.exists(self.output_csv):
                df = pd.read_csv(self.output_csv)
                st.write("Dữ liệu số công văn:")
                st.dataframe(df)
            else:
                st.warning("File số công văn chưa được tạo. Vui lòng cập nhật số công văn trước.")
        except Exception as e:
            st.error(f"Đã xảy ra lỗi: {e}")

# Hàm hiển thị tạo file số công văn
def hien_thi_tao_file_so_cong_van():
    # Nhập đường dẫn thư mục chứa các file Excel và đường dẫn file CSV đầu ra
    directory = st.text_input('Nhập đường dẫn thư mục chứa các file Excel:', r'G:\My Drive\dung_data\vanbancapnhat')
    output_csv = st.text_input('Nhập đường dẫn file CSV đầu ra:', r'G:\My Drive\Obsidian_dung\02 du an\dung_qldt_phuctho\data\socongvan.csv')

    # Tạo đối tượng HienThiFileSoCongVan
    hien_thi_cong_van = HienThiFileSoCongVan(directory, output_csv)

    # Nút cập nhật số công văn
    if st.button('Cập nhật số công văn'):
        hien_thi_cong_van.cap_nhat_so_cong_van()

    # Nút hiển thị số công văn
    if st.button('Hiển thị số công văn'):
        hien_thi_cong_van.hien_thi_so_cong_van()

