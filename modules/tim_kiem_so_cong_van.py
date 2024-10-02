# modules/tim_kiem_so_cong_van.py
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd
import io
from typing import Tuple
from typing import List

class TimKiemSoCongVan:
    """
    Lớp xử lý dữ liệu từ file CSV và thực hiện các thao tác lọc dữ liệu.
    """

    def __init__(self, file_path: str):
        """
        Khởi tạo đối tượng xử lý dữ liệu với đường dẫn đến file CSV.
        :param file_path: Đường dẫn file CSV
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

   
    def loc_du_lieu_so_cong_van(self, trich_yeu: List[str], loai_bo_trich_yeu: List[str], 
                    so_ky_hieu: List[str], loai_bo_so_ky_hieu: List[str], 
                    ngay_van_ban: List[str], chu_thuong_khong_dau) -> pd.DataFrame:
        """
        Lọc dữ liệu dựa trên các tiêu chí tìm kiếm.
        :param trich_yeu: Danh sách từ khóa trong trích yếu
        :param loai_bo_trich_yeu: Danh sách từ khóa cần loại bỏ trong trích yếu
        :param so_ky_hieu: Danh sách từ khóa trong số ký hiệu
        :param loai_bo_so_ky_hieu: Danh sách từ khóa cần loại bỏ trong số ký hiệu
        :param ngay_van_ban: Danh sách từ khóa trong ngày văn bản
        :param chu_thuong_khong_dau: Hàm chuyển đổi chuỗi thành không dấu
        :return: DataFrame chứa dữ liệu đã được lọc
        """
        df_loc_du_lieu_so_cong_van = self.df[self.df['Trích yếu'].apply(chu_thuong_khong_dau).str.contains('|'.join(trich_yeu), case=False) 
                        & ~self.df['Trích yếu'].apply(chu_thuong_khong_dau).str.contains('|'.join(loai_bo_trich_yeu), na=False)
                        & self.df['Số ký hiệu'].apply(chu_thuong_khong_dau).apply(lambda x: all(chuoi in x for chuoi in so_ky_hieu))
                        & ~self.df['Số ký hiệu'].apply(chu_thuong_khong_dau).str.contains('|'.join(loai_bo_so_ky_hieu), na=False)
                        & self.df['Ngày văn bản'].apply(chu_thuong_khong_dau).str.contains('|'.join(ngay_van_ban), case=False)]
        return df_loc_du_lieu_so_cong_van
    
    def tao_bo_loc() -> Tuple[str, str, str, str, str]:
        """
        Tạo các thành phần bộ lọc trong giao diện.
        :return: Bộ giá trị từ các input của người dùng
        """
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            trich_yeu = st.text_input('Lọc theo Nội dung trích yếu', 'Về việc')
        with col2:
            loai_bo_trich_yeu = st.text_input('Loại bỏ nội dung có trong trích yếu', '@@@')
        with col3:
            so_ky_hieu = st.text_input('Lọc theo Số ký hiệu', 'qldt')
        with col4:
            loai_bo_so_ky_hieu = st.text_input('Loại bỏ nội dung có trong số ký hiệu', '@@@')
        with col5:
            ngay_van_ban = st.text_input('Lọc theo Ngày văn bản', '2024')

        return trich_yeu, loai_bo_trich_yeu, so_ky_hieu, loai_bo_so_ky_hieu, ngay_van_ban
    
    def hien_thi_data_frame(df: pd.DataFrame) -> None:
        """
        Hiển thị bảng dữ liệu với tính năng phân trang và tùy chỉnh.
        :param df: DataFrame chứa dữ liệu để hiển thị
        """
        gb = GridOptionsBuilder.from_dataframe(df)
        gb.configure_pagination(paginationAutoPageSize=True)
        gb.configure_default_column(wrapText=True, autoHeight=True)
        gridOptions = gb.build()

        st.write("Kết quả tìm kiếm và tra cứu:")
        AgGrid(df, gridOptions=gridOptions, height=400, fit_columns_on_grid_load=True)

    def nut_tai_xuong(df: pd.DataFrame) -> None:
        """
        Tạo nút tải xuống file Excel chứa kết quả tìm kiếm.
        :param df: DataFrame chứa dữ liệu cần tải xuống
        """
        excel_buffer = io.BytesIO()
        with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Dữ liệu')
        excel_data = excel_buffer.getvalue()

        st.download_button(
            label="Tải xuống danh sách kết quả tìm kiếm",
            data=excel_data,
            file_name='du_lieu.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
  