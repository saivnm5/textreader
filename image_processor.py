import cv2
import numpy as np
from PIL import Image
from typing import Optional, Tuple
import os
from text_extractor import TextExtractor

class ImageProcessor:
    def __init__(self, text_extractor: TextExtractor):
        self.text_extractor = text_extractor

    def process_image(self, image_path: str, canvas_scope: Optional[Tuple[int, int, int, int]], text_type: str, output_text_file: str, output_image_file: str) -> str:
        # Extract text from image
        extracted_text = self.text_extractor.extract(image_path, canvas_scope, text_type)
        
        if canvas_scope:
            # Read and crop the image
            image = cv2.imread(image_path)
            if image is None:
                raise ValueError(f"Image at path {image_path} could not be loaded.")
            
            cropped_image = self._crop_image(image, canvas_scope)
            # Save the cropped image
            self._save_image(cropped_image, output_image_file)
        
        # Save the extracted text
        with open(output_text_file, 'w', encoding='utf-8') as f:
            f.write(extracted_text)
        
        return extracted_text

    def _crop_image(self, image: np.ndarray, canvas_scope: Optional[Tuple[int, int, int, int]]) -> np.ndarray:
        if canvas_scope:
            x, y, w, h = canvas_scope
            x = max(0, x)
            y = max(0, y)
            h = min(image.shape[0], y + h)
            w = min(image.shape[1], x + w)
            cropped_image = image[y:h, x:w]
            
            # Handle case where cropping might result in an invalid image
            if cropped_image.size == 0 or cropped_image.shape[0] <= 0 or cropped_image.shape[1] <= 0:
                raise ValueError("Cropping resulted in an invalid image.")
                
            return cropped_image
        return image

    def _save_image(self, image: np.ndarray, output_image_file: str) -> None:
        # Convert BGR (OpenCV format) to RGB (PIL format)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Convert numpy array to PIL image
        pil_image = Image.fromarray(image_rgb)
        
        # Ensure the output directory exists
        output_dir = os.path.dirname(output_image_file)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Save the image
        try:
            pil_image.save(output_image_file, format='PNG')
        except Exception as e:
            raise RuntimeError(f"Failed to save image: {e}")
