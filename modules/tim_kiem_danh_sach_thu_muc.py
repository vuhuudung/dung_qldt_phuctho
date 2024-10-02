# modules/tim_kiem_danh_sach_thu_muc.py

import pandas as pd
from typing import List
import os
import streamlit as st

class TimKiemDanhSachThuMuc:
    """
    Lớp cung cấp các chức năng tìm kiếm và quản lý danh sách thư mục.
    """

    def __init__(self, file_path: str):
        """
        Khởi tạo đối tượng tìm kiếm danh sách thư mục với đường dẫn đến file CSV.
        :param file_path: Đường dẫn file CSV chứa thông tin thư mục
        """
        self.file_path = file_path
        self.df = self.load_data()

    def load_data(self) -> pd.DataFrame:
        """
        Đọc dữ liệu từ file CSV và trả về dưới dạng DataFrame.
        :return: DataFrame chứa dữ liệu từ file CSV
        """
        df = pd.read_csv(self.file_path, header=0, dtype=str)
        return df.astype(str)

    def loc_du_lieu_danh_sach_thu_muc(self, so_ky_hieu: List[str], chu_thuong_khong_dau) -> pd.DataFrame:
        """
        Lọc danh sách thư mục dựa trên từ khóa tìm kiếm.
        :param so_ky_hieu: Danh sách các từ khóa tìm kiếm thư mục
        :param chu_thuong_khong_dau: Hàm chuyển đổi chuỗi thành không dấu
        :return: DataFrame chứa danh sách thư mục đã được lọc
        """
        df_loc_du_lieu_danh_sach_thu_muc = self.df[self.df['Folder Name'].apply(chu_thuong_khong_dau).apply(lambda x: all(chuoi in x for chuoi in so_ky_hieu))]
        return df_loc_du_lieu_danh_sach_thu_muc

    def mo_thu_muc(self, path: str) -> None:
        """
        Mở thư mục trên hệ thống nếu tồn tại.
        :param path: Đường dẫn đến thư mục cần mở
        """
        if os.path.exists(path):
            os.startfile(path)  # Chỉ hoạt động trên Windows
        else:
            st.error(f"Đường dẫn không tồn tại: {path}")

    def hien_thi_danh_sach_thu_muc(self, df_loc_du_lieu_danh_sach_thu_muc: pd.DataFrame) -> None:
        """
        Hiển thị danh sách các thư mục trong giao diện Streamlit và cho phép mở thư mục.
        :param df_loc: DataFrame chứa các thư mục đã được lọc
        """
        st.write("Chọn đường dẫn để mở Folder:")
        for index, row in df_loc_du_lieu_danh_sach_thu_muc.iterrows():
            col1, col2 = st.columns([4, 1])
            with col1:
                st.write(row['Full Path'])
            with col2:
                if st.button('Mở Folder', key=index):
                    self.mo_thu_muc(row['Full Path'])
