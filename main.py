from text_extractor import TextExtractor
from config import *

def main():
    text_extractor = TextExtractor()
    extracted_text = text_extractor.extract(IMAGE_PATH, CANVAS_SCOPE)
    print("Extracted Text:", extracted_text)

if __name__ == "__main__":
    main()



