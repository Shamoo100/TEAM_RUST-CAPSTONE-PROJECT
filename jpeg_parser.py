import os
import glob
from PIL import Image


def jpeg_parser(path):
    for filename in os.listdir(path):
        if not filename.endswith(("JPEG", 'jpeg', "JPG", 'jpg')):
            file = os.path.join(path, filename)
            im = Image.open(file)
            im.save(file.rsplit('.', 1)[0] + ".jpg")
            os.remove(file)
            
            
path = '/Users/salahudeentope/Desktop/images'
jpeg_parser(path)
print(os.listdir(path))
print(len(os.listdir(path)))