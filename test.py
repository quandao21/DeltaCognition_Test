# import easyocr

# reader = easyocr.Reader(['en'])
# result = reader.readtext('DaoThanhQuan_transcript.pdf', detail = 0)
# print(result)
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_document = fitz.open(pdf_path)

    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        text += page.get_text()

    pdf_document.close()
    return text

# # Replace this with the actual path to your PDF file
pdf_path = "DaoThanhQuan_CV.pdf"

extracted_text = extract_text_from_pdf(pdf_path)
print(extracted_text)

# from pdf2image import convert_from_path
# import pytesseract

# def extract_text_from_pdf(pdf_path):
#     text = ""
#     images = convert_from_path(pdf_path)

#     for i, image in enumerate(images):
#         image_text = pytesseract.image_to_string(image)
#         text += image_text

#     return text

# # Replace this with the actual path to your image-based PDF
# pdf_path = "DaoThanhQuan_transcript.pdf"

# extracted_text = extract_text_from_pdf(pdf_path)
# print(extracted_text)

# from PIL import Image
# import pytesseract

# file = Image.open("id.jpeg")
# str = pytesseract.image_to_string(file, lang='eng')

# print(str)


