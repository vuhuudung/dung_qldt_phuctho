import os
from pathlib import Path
import pandas as pd


def join_xlsx_to_csv(directory, output_csv, sheet_name='IncomingDocuments', header=5, **kwargs):
    """
    Kết hợp tất cả các file Excel trong thư mục chỉ định thành một DataFrame và lưu kết quả dưới dạng file CSV.

    :param directory: Đường dẫn đến thư mục chứa các file Excel.
    :param output_csv: Đường dẫn đến file CSV đầu ra.
    :param sheet_name: Tên sheet trong các file Excel cần đọc (mặc định là 'IncomingDocuments').
    :param header: Chỉ số hàng được sử dụng làm tiêu đề của các cột trong DataFrame (mặc định là 5). 
    :param **kwargs: Các tham số khác được truyền vào hàm pd.read_excel, như `dtype`, `skiprows`, `usecols`, v.v.
    
    :return: DataFrame chứa toàn bộ dữ liệu từ các file Excel đã kết hợp.
    """
    try:
        def list_excel_files(directory):
            """Liệt kê tất cả các file Excel trong thư mục."""
            path = Path(directory)
            excel_files = [f.name for f in path.glob('*.xlsx')]
            return excel_files

        excel_files = list_excel_files(directory)
        df = pd.DataFrame()

        for file_excel in excel_files:
            file_path = os.path.join(directory, file_excel)
            df_excel = pd.read_excel(file_path, sheet_name=sheet_name, header=header, dtype=str, **kwargs)
            
            # Thêm dữ liệu vào DataFrame chính
            df = pd.concat([df, df_excel], axis=0)

        # Chuyển đổi chuỗi ngày tháng năm thành định dạng datetime
        df['Ngày văn bản'] = pd.to_datetime(df['Ngày văn bản'], format='%d/%m/%Y', errors='coerce')

        # Sắp xếp theo cột 'Ngày văn bản'
        df = df.sort_values(by='Ngày văn bản')

        # Định dạng lại cột 'Ngày văn bản' thành chuỗi với định dạng ngày/tháng/năm
        df['Ngày văn bản'] = df['Ngày văn bản'].dt.strftime('%d/%m/%Y')

        # Xóa các hàng trùng lặp, giữ lại hàng cuối cùng cho mỗi nhóm trùng lặp
        df = df.drop_duplicates(subset=['Trích yếu', 'Số ký hiệu', 'Ngày văn bản'], keep='last')

        # Thêm cột 'STT' với chỉ số hàng
        df['STT'] = df.index

        # Lưu DataFrame kết quả dưới dạng CSV với các tùy chọn phù hợp để tránh lỗi định dạng
        df.to_csv(output_csv, index=False, encoding='utf-8-sig')

        # Trả về DataFrame
        return df

    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
        return None



def list_folders_to_csv(folder_path, csv_file, **kwargs):
    """
    Liệt kê các thư mục con trong các thư mục con thuộc thư mục gốc, và lưu thông tin vào một file CSV. 
    Đồng thời, trả về DataFrame chứa thông tin về các thư mục.

    :param folder_path: Đường dẫn đến thư mục gốc.
    :param csv_file: Đường dẫn đến file CSV nơi lưu danh sách các thư mục.
    :param **kwargs: Các tham số bổ sung cho hàm `pd.DataFrame.to_csv`, như `sep`, `encoding`, `index`, v.v.
    
    :return: DataFrame chứa thông tin về các thư mục.
    """
    try:
        # Tạo danh sách để chứa tên và địa chỉ thư mục
        folder_names = []
        folder_addresses = []

        # Duyệt qua các thư mục con của thư mục gốc
        for folder_name in os.listdir(folder_path):
            full_path = os.path.join(folder_path, folder_name)
            if os.path.isdir(full_path):
                # Duyệt qua các thư mục con bên trong thư mục con này
                for subfolder_name in os.listdir(full_path):
                    subfolder_full_path = os.path.join(full_path, subfolder_name)
                    if os.path.isdir(subfolder_full_path):
                        folder_names.append(subfolder_name)
                        folder_addresses.append(subfolder_full_path)

        # Tạo DataFrame từ danh sách các thư mục
        df_folders = pd.DataFrame({
            'Folder Name': folder_names,
            'Full Path': folder_addresses
        })

        # Xóa tệp CSV cũ nếu nó tồn tại
        if os.path.exists(csv_file):
            os.remove(csv_file)

        # Lưu DataFrame vào tệp CSV với các tùy chọn bổ sung từ **kwargs
        df_folders.to_csv(csv_file, index=False, encoding='utf-8-sig', **kwargs)

        print("DataFrame đã được lưu vào file CSV thành công.")
        
        # Trả về DataFrame
        return df_folders

    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
        return None


