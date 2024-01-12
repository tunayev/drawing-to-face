import os
from PIL import Image

class Cropper:
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.image_path = image_path

    def crop(self, width, height, top_offset=None, left_offset=None):
        img_width, img_height = self.image.size

        if top_offset is None:
            top_offset = (img_height - height) // 2

        if left_offset is None:
            left_offset = (img_width - width) // 2

        right = left_offset + width
        bottom = top_offset + height

        cropped_image = self.image.crop((left_offset, top_offset, right, bottom))
        return cropped_image

    def resize(self, image, width, height):
        resized_image = image.resize((width, height))
        return resized_image

    def save_image(self, image, output_dir):
        filename = os.path.basename(self.image_path)
        output_path = os.path.join(output_dir, filename)
        image.save(output_path)