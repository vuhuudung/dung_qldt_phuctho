# main.py

import streamlit as st
from giaodien.hien_thi_tim_kiem_so_cong_van import *
from giaodien.hien_thi_tim_kiem_danh_sach_thu_muc import *
from giaodien.hien_thi_thong_tin_ung_dung import *
from giaodien.hien_thi_chuyen_doi_pdf_sang_text import *
from giaodien.hien_thi_tao_file_danh_sach_thu_muc import *
from giaodien.hien_thi_tao_file_so_cong_van import *
from giaodien.hien_thi_tim_kiem_tuyet_doi import *
from giaodien.hien_thi_tim_kiem_tuong_doi import *
from giaodien.hien_thi_to_chuc_file import *

###########################################################
def render():
    st.set_page_config(layout="wide")
    # st.title('web app streamlit hỗ trợ công việc')
    # st.header('web app streamlit hỗ trợ công việc')
    st.subheader('Welome to my website! Have a nice day abc!')
    st.text('Tác giả: Vũ Hữu Dũng - CV phòng QLĐT')
    st.markdown('---')
###########################################################
    selected_menu = st.sidebar.radio("Chọn chức năng", ["Tìm kiếm","Tổ chức file", "Tạo file dữ liệu", "Chuyển đổi pdf sang text","Thông tin ứng dụng"])

    if selected_menu == "Tìm kiếm":
        # Tab tìm kiếm sẽ bao gồm hai phần: tìm kiếm công văn và tìm kiếm thư mục
        tab1, tab2, tab3, tab4 = st.tabs(["Tìm kiếm theo số công văn",
                              "Tìm kiếm theo tên thư mục",
                              "Tim kiếm tuyệt đối tên thư mục và tên file",
                              "Tỉm kiếm tương đối tên thư mục và tên file"])
        
        with tab1:
            st.subheader("Tìm kiếm số công văn")
            hien_thi_tim_kiem_so_cong_van()

        with tab2:
            st.subheader("Tìm kiếm theo thư mục")
            hien_thi_tim_kiem_danh_sach_thu_muc()

        with tab3:
            st.subheader("Tim kiếm tuyệt đối tên thư mục và tên file")
            hien_thi_tim_kiem_tuyet_doi()
        
        with tab4:
            st.subheader("Tim kiếm tương đối tên thư mục và tên file")
            hien_thi_tim_kiem_tuong_doi()
    
    elif selected_menu == "Tổ chức file":
        # Hiển thị thông tin ứng dụng
        hien_thi_to_chuc_file()
    elif selected_menu == "Tạo file dữ liệu":
        # Tab tạo file dữ liệu bao gồm hai phần: tạo file socongvan.csv và danhsachthumuc.csf
        tab1, tab2 = st.tabs(["Tạo file socongvan.csv", "Tạo file danhsachthumuc.csv"])
        
        with tab1:
            st.subheader("Tạo file socongvan.csv")
            hien_thi_tao_file_so_cong_van()

        with tab2:
            st.subheader("Tạo file danhsachthumuc.csv")
            hien_thi_tao_file_danh_sach_thu_muc()
    
    elif selected_menu == "Chuyển đổi pdf sang text":
        # Hiển thị thông tin ứng dụng
        hien_thi_chuyen_doi_pdf_sang_text()

    elif selected_menu == "Thông tin ứng dụng":
        # Hiển thị thông tin ứng dụng
        hien_thi_thong_tin_ung_dung()

if __name__ == "__main__":
    render()




















# # Cài đặt thư viện
# import streamlit as st
# import pandas as pd
# import numpy as np
# import unidecode
# import os
# import requests
# import io
# from io import BytesIO
# from st_aggrid import AgGrid, GridOptionsBuilder
# import webbrowser
# from pathlib import Path

# def render():
#     # Thiết lập wide mode cho Streamlit
#     st.set_page_config(layout="wide")

#     st.header('WEBAPP HỖ TRỢ CÔNG VIỆC')
#     st.text('Tác giả: Vũ Hữu Dũng - CV phòng QLĐT')
# ####################################
#     file_socongvan_csv= r'data/socongvan.csv'
#     df=pd.read_csv(file_socongvan_csv, header=0, dtype=str) #lấy dữ liệu, không lấy header

#     df=pd.DataFrame(df)
#     df=df.astype(str)
    
#     # Hàm loại bỏ dấu và chuyển về chữ thường
#     def chu_thuong_khong_dau(text):
#         return unidecode.unidecode(text).lower()

#     # Hàm chuyển đổi danh sách
#     def chuyen_doi_chu_thuong(lst):
#         return [chu_thuong_khong_dau(item) for item in lst]
    
#     # Nhập dữ liệu tìm kiếm
#     trich_yeu = 'Về việc' # str.contains để kiểm tra hoặc có có chuỗi này không
#     loai_bo_trich_yeu = '@@@'
#     so_ky_hieu = 'qldt' #.apply để kiểm tra có đồng thời các chuỗi này không
#     loai_bo_so_ky_hieu = '@@@'
#     ngay_van_ban = '2024' # str.contains để kiểm tra hoặc có có chuỗi này không

# ####################################
#     # Add 2 columns for date input
#     col1, col2, col3, col4, col5 = st.columns(5)

#     with col1:
#         trich_yeu = st.text_input('Lọc theo Nội dung trích yếu', trich_yeu)

#     with col2:
#         loai_bo_trich_yeu = st.text_input('Loại bỏ nội dung có trong trích yếu', loai_bo_trich_yeu)

#     with col3:
#         so_ky_hieu = st.text_input('Lọc theo Số ký hiệu', so_ky_hieu)

#     with col4:
#         loai_bo_so_ky_hieu = st.text_input('Loại bỏ nội dung có trong số ký hiệu', loai_bo_so_ky_hieu)

#     with col5:
#         ngay_van_ban = st.text_input('Lọc theo Ngày văn bản', ngay_van_ban)

#     # chuyển đổi kiểu chữ   
#     trich_yeu = chuyen_doi_chu_thuong([item.strip() for item in trich_yeu.split(',')])
#     loai_bo_trich_yeu = chuyen_doi_chu_thuong([item.strip() for item in loai_bo_trich_yeu.split(',')])
#     so_ky_hieu = chuyen_doi_chu_thuong([item.strip() for item in so_ky_hieu.split(',')])
#     loai_bo_so_ky_hieu = chuyen_doi_chu_thuong([item.strip() for item in loai_bo_so_ky_hieu.split(',')])
#     ngay_van_ban = chuyen_doi_chu_thuong([item.strip() for item in ngay_van_ban.split(',')])

#     # Tìm kiếm và lọc các dòng chứa ít nhất một trong các chuỗi cần lọc
#     df_loc = df[df['Trích yếu'].apply(chu_thuong_khong_dau).str.contains('|'.join(trich_yeu),case=False) 
#                 & ~df['Trích yếu'].apply(chu_thuong_khong_dau).str.contains('|'.join(loai_bo_trich_yeu), na=False)
#                 & df['Số ký hiệu'].apply(chu_thuong_khong_dau).apply(lambda x: all(chuoi in x for chuoi in so_ky_hieu))
#                 & ~df['Số ký hiệu'].apply(chu_thuong_khong_dau).str.contains('|'.join(loai_bo_so_ky_hieu), na=False)
#                 & df['Ngày văn bản'].apply(chu_thuong_khong_dau).str.contains('|'.join(ngay_van_ban),case=False) 
#     ]
    
#     # Hiển thị kết quả
#     df_hienthi = df_loc[['Trích yếu', 'Số ký hiệu', 'Ngày văn bản', 'Đơn vị ban hành', 'Ghi chú']]
    
#     # Sử dụng st_aggrid để tùy chỉnh chiều rộng của từng cột
#     gb = GridOptionsBuilder.from_dataframe(df_hienthi)

#     # Cấu hình chiều rộng của từng cột
#     # gb.configure_column("STT", width=10, sortable=True)
#     gb.configure_column("Trích yếu", width=100, sortable=True)
#     gb.configure_column("Số ký hiệu", width=10, sortable=True)
#     gb.configure_column("Ngày văn bản", width=10, sortable=True)
#     gb.configure_column("Đơn vị ban hành", width=10, sortable=True)
#     gb.configure_column("Ghi chú", width=10, sortable=True)
    
#     # Cấu hình phân trang
#     gb.configure_pagination(paginationAutoPageSize=True)  # Chia thành nhiều trang tự động
#     gb.configure_default_column(wrapText=True, autoHeight=True)  # Tự động giãn ô khi chuỗi dài
#     gridOptions = gb.build()

#     # Hiển thị DataFrame với cấu hình tùy chỉnh
#     st.write("Kết quả tìm kiếm và tra cứu:")
#     AgGrid(df_hienthi, gridOptions=gridOptions, height=400, fit_columns_on_grid_load=True)
#         # Tạo nút tải xuống Excel
#     excel_buffer = io.BytesIO()
#     with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
#         df_hienthi.to_excel(writer, index=False, sheet_name='Dữ liệu')
#     excel_data = excel_buffer.getvalue()

#     st.download_button(
#         label="Tải xuống danh sách kết quả tìm kiếm",
#         data=excel_data,
#         file_name='du_lieu.xlsx',
#         mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
#     ) 

# ####################################
#     path_file= r'data/danhsachthumuc.csv'
#     df_path=pd.read_csv(path_file, header=0, dtype=str)

#     df_path=pd.DataFrame(df_path)
#     df_path=df_path.astype(str)

#     so_ky_hieu_2 = '000, cv, qldt, dung, 2024' #.apply để kiểm tra có đồng thời các chuỗi này không
#     so_ky_hieu_2 = st.text_input('Tìm kiếm theo tên thư mục', so_ky_hieu_2)
#     so_ky_hieu_2 = chuyen_doi_chu_thuong([item.strip() for item in so_ky_hieu_2.split(',')])
#     # Tìm kiếm và lọc các dòng chứa ít nhất một trong các chuỗi cần lọc
#     df_path_loc = df_path[df_path['Folder Name'].apply(chu_thuong_khong_dau).apply(lambda x: all(chuoi in x for chuoi in so_ky_hieu_2))]
    
#     # Sử dụng st_aggrid để tùy chỉnh chiều rộng của từng cột
#     gb1 = GridOptionsBuilder.from_dataframe(df_path_loc)

# ########################################
#     # Hàm mở đường dẫn local
#     def open_local_path(path):
#         if os.path.exists(path):
#             os.startfile(path)  # Đối với Windows
#             # webbrowser.open(path)  # Đối với các hệ điều hành khác
#         else:
#             st.error(f"Đường dẫn không tồn tại: {path}")

#     st.write("Chọn đường dẫn để mở Folder:")
#     for index, row in df_path_loc.iterrows():
#         col1, col2 = st.columns([4, 1])
#         with col1:
#             st.write(row['Full Path'])
#         with col2:
#             if st.button('Mở Folder', key=index):
#                 open_local_path(row['Full Path'])
        

# render()

