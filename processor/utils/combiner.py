import os
from PIL import Image

class Combiner:
    def __init__(self, image_a_path, image_b_path):
        self.image_a = Image.open(image_a_path)
        self.image_b = Image.open(image_b_path)
        self.image_a_path = image_a_path
        self.image_b_path = image_b_path
        
    def combine(self):
        image_a_width, image_a_height = self.image_a.size
        image_b_width, image_b_height = self.image_b.size
        if image_a_width != image_b_width or image_a_height != image_b_height:
            raise Exception("Images must have the same dimensions")
        new_image = Image.new("RGB", (image_a_width * 2, image_a_height))
        new_image.paste(self.image_a, (0, 0))
        new_image.paste(self.image_b, (image_a_width, 0))
        return new_image
    
    def save_image(self, image, output_dir):
        filename = os.path.basename(self.image_a_path)
        output_path = os.path.join(output_dir, filename)
        image.save(output_path)
    
