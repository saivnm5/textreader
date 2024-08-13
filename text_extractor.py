import pytesseract
from pytesseract import Output
import regex as re
import cv2
from typing import Optional, Tuple, Dict

class TextExtractor:
    def extract(self, image_path: str, canvas_scope: Optional[Tuple[int, int, int, int]]) -> str:
        raise NotImplementedError

class TextExtractor(TextExtractor):

    def extract(self, image_path: str, canvas_scope: Optional[Tuple[int, int, int, int]]) -> str:
        image = cv2.imread(image_path)
        cropped_image = self._crop_image(image, canvas_scope)
        custom_config = r'--psm 6'
        data = pytesseract.image_to_data(cropped_image, output_type=Output.DICT, config=custom_config)
        return data['text']

    def _crop_image(self, image, canvas_scope: Optional[Tuple[int, int, int, int]]) -> 'np.ndarray':
        if canvas_scope:
            x, y, w, h = canvas_scope
            return image[y:y+h, x:x+w]
        return image

