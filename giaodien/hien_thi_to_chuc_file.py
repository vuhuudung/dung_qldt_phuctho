import os
import shutil
from pathlib import Path
import streamlit as st

def try_remove_read_only(func, path, exc_info):
    """Thay đổi quyền truy cập để có thể xóa tệp hoặc thư mục nếu gặp lỗi quyền."""
    import stat
    os.chmod(path, stat.S_IWUSR)
    func(path)

def organize_files(directory, destination_dir):
    """Tổ chức các file trong thư mục bằng cách tạo các thư mục con theo tên file và di chuyển file vào các thư mục này.

    Args:
        directory (str or Path): Đường dẫn đến thư mục chứa các file cần sắp xếp.
        destination_dir (str or Path): Đường dẫn đến thư mục đích nơi các file sẽ được di chuyển vào.
    """
    # Lấy danh sách tất cả các file trong thư mục
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    for file in files:
        # Tạo tên thư mục dựa trên tên file (loại bỏ phần mở rộng)
        folder_name = os.path.splitext(file)[0]
       
        # Tách tên file thành các phần dựa trên dấu cách
        file_name_parts = folder_name.split(' ')

        # Kiểm tra nếu tên file có ít nhất 5 phần
        if len(file_name_parts) >= 5:
            # Chuỗi thứ 5 trong tên file sẽ làm tên thư mục
            nam = file_name_parts[4]
        else:
            # Nếu không có chuỗi thứ 5, đặt một tên thư mục mặc định
            nam = "20xx"
        
        # Đường dẫn thư mục đích
        folder_path = Path(destination_dir)/nam/folder_name

        # Xóa thư mục cũ nếu đã tồn tại
        if folder_path.exists() and folder_path.is_dir():
            try:
                shutil.rmtree(folder_path, onerror=try_remove_read_only)
            except Exception as e:
                st.error(f"Có lỗi xảy ra khi xóa thư mục {folder_path}: {e}")
        
        # Tạo thư mục mới    
        folder_path.mkdir(parents=True, exist_ok=True)

        # Di chuyển file vào thư mục mới tạo
        file_path = os.path.join(directory, file)
        try:
            shutil.move(file_path, folder_path / file)
            st.write(f"Chuyển thành công: {file} -> {folder_path}")
        except PermissionError as e:
            st.error(f"Không thể di chuyển tệp {file_path}. Lỗi: {e}")
        except Exception as e:
            st.error(f"Có lỗi xảy ra với tệp {file_path}: {e}")

def hien_thi_to_chuc_file():
    """Giao diện tổ chức file với Streamlit."""
    st.title("Tổ chức file vào thư mục con")

    # Nhập đường dẫn thư mục nguồn và đích
    directory = st.text_input("Nhập đường dẫn thư mục chứa các file cần tổ chức:", value=r'C:\Users\admin\Desktop\New folder')
    destination_dir = st.text_input("Nhập đường dẫn thư mục đích:", value=r'D:\PC QLDT\ho so cong viec')

    # Nút để thực hiện tổ chức file
    if st.button("Tổ chức file"):
        if os.path.exists(directory) and os.path.exists(destination_dir):
            organize_files(directory, destination_dir)
        else:
            st.error("Vui lòng kiểm tra lại đường dẫn thư mục.")
