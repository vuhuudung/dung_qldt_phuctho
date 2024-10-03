import streamlit as st
from modules.tim_kiem_so_cong_van import TimKiemSoCongVan
from modules.chuyen_doi_chu_thuong_khong_dau import ChuyenDoiChuThuongKhongDau

def hien_thi_tim_kiem_so_cong_van():
    """
    Tìm kiếm công văn dựa trên các tiêu chí.
    """
    # Khởi tạo đối tượng tìm kiếm công văn
    tim_kiem_so_cong_van = TimKiemSoCongVan('data/socongvan.csv')

    # Lấy dữ liệu bộ lọc
    trich_yeu, loai_bo_trich_yeu, so_ky_hieu, loai_bo_so_ky_hieu, ngay_van_ban = TimKiemSoCongVan.tao_bo_loc()

    # Chuyển đổi các giá trị bộ lọc
    trich_yeu = ChuyenDoiChuThuongKhongDau.chuyen_doi_chu_thuong([item.strip() for item in trich_yeu.split(',')])
    loai_bo_trich_yeu = ChuyenDoiChuThuongKhongDau.chuyen_doi_chu_thuong([item.strip() for item in loai_bo_trich_yeu.split(',')])
    so_ky_hieu = ChuyenDoiChuThuongKhongDau.chuyen_doi_chu_thuong([item.strip() for item in so_ky_hieu.split(',')])
    loai_bo_so_ky_hieu = ChuyenDoiChuThuongKhongDau.chuyen_doi_chu_thuong([item.strip() for item in loai_bo_so_ky_hieu.split(',')])
    ngay_van_ban = ChuyenDoiChuThuongKhongDau.chuyen_doi_chu_thuong([item.strip() for item in ngay_van_ban.split(',')])

    # Lọc dữ liệu công văn
    df_loc_cong_van = tim_kiem_so_cong_van.loc_du_lieu_so_cong_van(trich_yeu, loai_bo_trich_yeu, so_ky_hieu, loai_bo_so_ky_hieu, ngay_van_ban, ChuyenDoiChuThuongKhongDau.chu_thuong_khong_dau)
    
    # Hiển thị kết quả công văn
    df_hien_thi_so_cong_van = df_loc_cong_van[['Trích yếu', 'Số ký hiệu', 'Ngày văn bản', 'Đơn vị ban hành', 'Ghi chú']]
    TimKiemSoCongVan.hien_thi_data_frame(df_hien_thi_so_cong_van)

    # Nút tải xuống kết quả công văn
    TimKiemSoCongVan.nut_tai_xuong(df_hien_thi_so_cong_van)