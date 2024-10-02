# modules/quan_ly_file.py

import os
import streamlit as st

class QuanLyFile:
    """
    Lớp cung cấp các chức năng quản lý file và thư mục.
    """

    @staticmethod
    def mo_duong_dan_local(path: str) -> None:
        """
        Mở đường dẫn thư mục trên hệ thống.
        :param path: Đường dẫn đến thư mục cần mở
        """
        if os.path.exists(path):
            os.startfile(path)  # Chỉ hoạt động trên Windows
        else:
            st.error(f"Đường dẫn không tồn tại: {path}")
