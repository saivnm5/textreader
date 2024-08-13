import pytesseract
from pytesseract import Output
import regex as re
import cv2
from typing import Optional, Tuple, Dict

class TextExtractor:
    def extract(self, image_path: str, canvas_scope: Optional[Tuple[int, int, int, int]], text_type: str) -> str:
        raise NotImplementedError

class PytesseractTextExtractor(TextExtractor):
    def __init__(self, tesseract_cmd: str):
        self.tesseract_cmd = tesseract_cmd
        pytesseract.pytesseract.tesseract_cmd = self.tesseract_cmd

    def extract(self, image_path: str, canvas_scope: Optional[Tuple[int, int, int, int]], text_type: str) -> str:
        image = cv2.imread(image_path)
        cropped_image = self._crop_image(image, canvas_scope)
        custom_config = r'--psm 6'
        data = pytesseract.image_to_data(cropped_image, output_type=Output.DICT, config=custom_config)

        print(data['text'])

        if text_type == 'title':
            extracted_text = self._extract_title(data)
        else:
            extracted_text = self._extract_full_text(data)

        return self._clean_text(extracted_text)

    def _crop_image(self, image, canvas_scope: Optional[Tuple[int, int, int, int]]) -> 'np.ndarray':
        if canvas_scope:
            x, y, w, h = canvas_scope
            return image[y:y+h, x:x+w]
        return image

    def _extract_title(self, data: Dict[str, list]) -> str:
        font_sizes = [(size, idx) for idx, (size, text) in enumerate(zip(data['height'], data['text']))
                      if self._is_valid_text(text) and text.strip() != '']
        
        if font_sizes:
            font_sizes.sort(reverse=True, key=lambda x: x[0])
            largest_text_idx = font_sizes[0][1]
            if data['text'][largest_text_idx].strip() == '':
                largest_text_idx = font_sizes[1][1] if len(font_sizes) > 1 else largest_text_idx
            return data['text'][largest_text_idx]
        return ""

    def _extract_full_text(self, data: Dict[str, list]) -> str:
        return " ".join(text for text in data['text'] if self._is_valid_text(text))

    def _is_valid_text(self, text: str) -> bool:
        if len(text) <= 2:
            return not re.search(r'[^A-Za-z0-9\s.,!?\'"()@-]', text)
        return True
    
    def _clean_text(self, text: str) -> str:
        """
        Clean the text by removing unwanted special characters.
        This method keeps Unicode letters, numbers, and common punctuation.
        """
        # This regex keeps Unicode letters, numbers, spaces, and common punctuation.
        cleaned_text = re.sub(r'[^\p{L}\p{M}\p{N}\p{Zs}\p{Pd}\p{Pc}]', '', text, flags=re.UNICODE)
        return cleaned_text
