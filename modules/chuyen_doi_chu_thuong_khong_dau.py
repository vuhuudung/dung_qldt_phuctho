# modules/chuyen_doi_chu_thuong_khong_dau.py

import unidecode
from typing import List

class ChuyenDoiChuThuongKhongDau:
    """
    Lớp cung cấp các chức năng tìm kiếm và chuyển đổi chuỗi ký tự.
    """

    @staticmethod
    def chu_thuong_khong_dau(text: str) -> str:
        """
        Chuyển chuỗi ký tự thành chữ thường và bỏ dấu.
        :param text: Chuỗi ký tự đầu vào
        :return: Chuỗi ký tự sau khi chuyển đổi
        """
        return unidecode.unidecode(text).lower()

    @staticmethod
    def chuyen_doi_chu_thuong(lst: List[str]) -> List[str]:
        """
        Chuyển đổi tất cả các phần tử trong danh sách thành chữ thường và bỏ dấu.
        :param lst: Danh sách chuỗi ký tự đầu vào
        :return: Danh sách chuỗi sau khi chuyển đổi
        """
        return [ChuyenDoiChuThuongKhongDau.chu_thuong_khong_dau(item) for item in lst]
