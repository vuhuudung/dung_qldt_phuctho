import os
import streamlit as st

def search_tuyet_doi(directory, hints):
    """
    Tìm kiếm tất cả các tệp và thư mục trong thư mục chỉ định và các thư mục con của nó,
    phù hợp với danh sách gợi ý tên được cung cấp.

    :param directory: Đường dẫn thư mục để tìm kiếm.
    :param hints: Danh sách các gợi ý để tìm kiếm trong tên tệp và thư mục.
    :return: Danh sách các kết quả tìm kiếm (gồm cả thư mục và tệp).
    """
    results = []

    # Duyệt qua tất cả các thư mục và tệp trong directory
    for root, dirs, files in os.walk(directory):
        # Tìm kiếm trong các thư mục
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if all(hint.lower() in folder.lower() for hint in hints):
                results.append(f"Thư mục: {folder_path}")

        # Tìm kiếm trong các tệp
        for file in files:
            file_path = os.path.join(root, file)
            if all(hint.lower() in file.lower() for hint in hints):
                results.append(f"Tệp: {file_path}")

    return results

def hien_thi_tim_kiem_tuyet_doi():
    """
    Hiển thị giao diện tìm kiếm tuyệt đối trên Streamlit.
    """

    # Nhập đường dẫn thư mục và các gợi ý tìm kiếm
    directory_tuyet_doi = st.text_input("Nhập đường dẫn thư mục:", value=r"D:\PC QLDT", key="directory_input_tuyet_doi")
    hints_tuyet_doi = st.text_input("Nhập các gợi ý tìm kiếm (phân tách bằng dấu phẩy):", value="td qldt dung 2024, dc bcktkt", key="hints_input_tuyet_doi").split(",")

    # Nút thực hiện tìm kiếm
    if st.button("Tìm kiếm", key="search_button_tuyet_doi"):
        if directory_tuyet_doi and hints_tuyet_doi:
            results = search_tuyet_doi(directory_tuyet_doi, hints_tuyet_doi)
            if results:
                st.write("Kết quả tìm kiếm:")
                for result in results:
                    st.write(result)
            else:
                st.write("Không tìm thấy kết quả nào.")
        else:
            st.error("Vui lòng nhập đường dẫn và gợi ý tìm kiếm.")
