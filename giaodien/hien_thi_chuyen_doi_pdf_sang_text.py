import streamlit as st
import ocrmypdf
import fitz  # PyMuPDF
from io import BytesIO

def ocr_pdf(input_pdf_bytes):
    """Chuyển đổi file PDF bằng OCR và trả về dữ liệu PDF đã OCR."""
    input_pdf = BytesIO(input_pdf_bytes)
    output_pdf = BytesIO()
    
    # Thực hiện OCR
    ocrmypdf.ocr(input_pdf, output_pdf, language='vie', force_ocr=True)
    
    return output_pdf.getvalue()

def extract_text_from_pdf(pdf_bytes):
    """Trích xuất văn bản từ file PDF."""
    pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()

    return text

def hien_thi_chuyen_doi_pdf_sang_text():
    """Giao diện chuyển đổi PDF sang văn bản trực tiếp trong Streamlit."""
    st.title("Chuyển đổi PDF sang văn bản trực tiếp trên Streamlit")

    # Tải lên file PDF
    input_pdf = st.file_uploader("Chọn file PDF", type="pdf")

    if input_pdf is not None:
        input_pdf_bytes = input_pdf.read()

        # Khi nhấn nút "Chuyển đổi"
        if st.button("Chuyển đổi"):
            try:
                # Thực hiện OCR và trích xuất văn bản
                ocr_pdf_bytes = ocr_pdf(input_pdf_bytes)
                extracted_text = extract_text_from_pdf(ocr_pdf_bytes)
                
                # Hiển thị thông báo thành công
                st.success("Chuyển đổi thành công!")
                
                # Hiển thị nội dung văn bản trích xuất trực tiếp trên giao diện
                st.subheader("Nội dung văn bản đã trích xuất:")
                st.text_area("Nội dung PDF:", extracted_text, height=300)

            except Exception as e:
                st.error(f"Đã xảy ra lỗi: {e}")

