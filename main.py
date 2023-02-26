#!/usr/bin/python
from PIL import Image
import os

def convert(path):
    for filename in os.listdir(path):
        if filename.endswith(".webp"):
            im = Image.open(path + "/"  + filename)
            filename = (filename.replace("webp", ""))
            im.save(path + "/" + filename + ".png", "PNG")
            print("Converted " + filename)
            os.remove(path + "/" + filename + "webp")
if __name__ == "__main__":
    while True:
        yol = input("Enter path to images: \n")
        convert(yol)
