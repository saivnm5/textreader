from text_extractor import PytesseractTextExtractor
from image_processor import ImageProcessor

def main():
    tesseract_cmd = r'/opt/homebrew/bin/tesseract'  # Adjust this path to your Tesseract installation
    text_extractor = PytesseractTextExtractor(tesseract_cmd)
    image_processor = ImageProcessor(text_extractor)

    image_path = '../example.png'
    canvas_scope = (0, 200, 900, 600)  # Example canvas scope (x, y, width, height)
    text_type = 'title'  # Options: 'title' or 'fulltext'
    output_text_file = 'output/extracted_text.txt'
    output_image_file = 'output/canvas_area.jpg'

    extracted_text = image_processor.process_image(image_path, canvas_scope, text_type, output_text_file, output_image_file)
    print("Extracted Text:", extracted_text)

if __name__ == "__main__":
    main()





