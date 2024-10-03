import os
import pandas as pd
import streamlit as st
from modules.office import list_folders_to_csv  # Import hàm list_folders_to_csv từ thư viện dung_lib

class HienThiDanhSachThuMuc:
    """
    Lớp để xử lý việc liệt kê danh sách các thư mục và hiển thị kết quả.
    """

    def __init__(self, folder_path: str, csv_file: str):
        """
        Khởi tạo đối tượng với đường dẫn thư mục cần liệt kê và file CSV đầu ra.
        :param folder_path: Đường dẫn đến thư mục bạn muốn liệt kê các thư mục con.
        :param csv_file: Đường dẫn đến file CSV nơi bạn muốn lưu danh sách thư mục.
        """
        self.folder_path = folder_path
        self.csv_file = csv_file

    def tao_danh_sach_thu_muc(self):
        """
        Tạo danh sách các thư mục từ folder_path và lưu vào file CSV.
        """
        try:
            df_combined = list_folders_to_csv(self.folder_path, self.csv_file)
            if df_combined is not None:
                st.success("Tạo danh sách thư mục và lưu vào file CSV thành công.")
            else:
                st.error("Có lỗi xảy ra khi tạo danh sách thư mục.")
        except Exception as e:
            st.error(f"Đã xảy ra lỗi: {e}")

    def hien_thi_danh_sach_thu_muc(self):
        """
        Hiển thị nội dung file CSV danh sách các thư mục.
        """
        try:
            if os.path.exists(self.csv_file):
                df = pd.read_csv(self.csv_file)
                st.write("Dữ liệu danh sách thư mục:")
                st.dataframe(df)
            else:
                st.warning("File danh sách thư mục chưa được tạo. Vui lòng tạo danh sách trước.")
        except Exception as e:
            st.error(f"Đã xảy ra lỗi: {e}")

# Hàm hiển thị tạo file danh sách thư mục
def hien_thi_tao_file_danh_sach_thu_muc():

    # Nhập đường dẫn thư mục chứa các thư mục con và đường dẫn file CSV đầu ra
    folder_path = st.text_input('Nhập đường dẫn thư mục:', r"D:\PC QLDT\ho so cong viec")
    csv_file = st.text_input('Nhập đường dẫn file CSV đầu ra:', r'G:\My Drive\Obsidian_dung\02 du an\dung_qldt_phuctho\data\danhsachthumuc.csv')

    # Tạo đối tượng HienThiDanhSachThuMuc
    hien_thi_thu_muc = HienThiDanhSachThuMuc(folder_path, csv_file)

    # Nút tạo danh sách thư mục
    if st.button('Tạo danh sách thư mục'):
        hien_thi_thu_muc.tao_danh_sach_thu_muc()

    # Nút hiển thị danh sách thư mục
    if st.button('Hiển thị danh sách thư mục'):
        hien_thi_thu_muc.hien_thi_danh_sach_thu_muc()
