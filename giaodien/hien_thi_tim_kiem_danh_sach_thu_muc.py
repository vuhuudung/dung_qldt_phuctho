import streamlit as st
from modules.chuyen_doi_chu_thuong_khong_dau import ChuyenDoiChuThuongKhongDau
from modules.tim_kiem_danh_sach_thu_muc import TimKiemDanhSachThuMuc


def hien_thi_tim_kiem_danh_sach_thu_muc():
    # Khởi tạo đối tượng tìm kiếm danh sách thư mục
    tim_kiem_thu_muc = TimKiemDanhSachThuMuc('data/danhsachthumuc.csv')

    # Tìm kiếm thư mục
    ten_thu_muc = st.text_input('Tìm kiếm theo tên thư mục', '000, cv, qldt, dung, 2024')
    ten_thu_muc = ChuyenDoiChuThuongKhongDau.chuyen_doi_chu_thuong([item.strip() for item in ten_thu_muc.split(',')])

    # Lọc danh sách thư mục
    df_loc_danh_sach_thu_muc = tim_kiem_thu_muc.loc_du_lieu_danh_sach_thu_muc(ten_thu_muc, ChuyenDoiChuThuongKhongDau.chu_thuong_khong_dau)

    # Hiển thị danh sách thư mục
    tim_kiem_thu_muc.hien_thi_danh_sach_thu_muc(df_loc_danh_sach_thu_muc)