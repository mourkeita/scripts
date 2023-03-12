#!/usr/bin/python
# coding: utf8

'''
This script convert an image to black and white
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
python convert_image_to_black_and_white.py
'''

from PIL import Image

print("Converting...")

img = Image.open("kub.png")
result = img.convert("L")
result.save("kub-bw.png")
result.show()
