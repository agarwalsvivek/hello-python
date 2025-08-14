import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os

# sudo apt update
# sudo apt install poppler-utils

# sudo apt update
# sudo apt install tesseract-ocr

# Set tessdata path
os.environ["TESSDATA_PREFIX"] = "/usr/share/tesseract-ocr/4.00/tessdata/"


def ocr_scanned_pdf(pdf_path):
    # Convert PDF pages to images
    images = convert_from_path(pdf_path)

    full_text = ""

    for i, image in enumerate(images):
        text = pytesseract.image_to_string(image)
        full_text += f"\n--- Page {i+1} ---\n{text}"

    return full_text

# Example usage
if __name__ == "__main__":
    pdf_file = "./hello_world.pdf"  # Replace with your scanned PDF path
    extracted_text = ocr_scanned_pdf(pdf_file)
    print("Extracted OCR Text:\n", extracted_text)
