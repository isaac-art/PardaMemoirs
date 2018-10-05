import os
import pytesseract
from PIL import Image
from pathlib import Path
from os.path import basename
from tomorrow import threads

# https://pypi.org/project/pytesseract/
# print(pytesseract.image_to_string(Image.open('scans/1.jpeg')))


def saveText(filename, text):
    with open("texts/%s.txt" % os.path.splitext(filename)[0], "w") as text_file:
        text_file.write("%s" % text)
    return
    

def checkNum(filename):
    file = "texts/%s.txt" % os.path.splitext(filename)[0]
    my_file = Path(file)
    if my_file.is_file():
        return False
    else:
        return True


@threads(20)
def getText(filename):
    if checkNum(filename):
        text = pytesseract.image_to_string(Image.open('scans/%s' % filename))
        saveText(filename, text)
    else:
        print("processed")
    return


def main(dir):
    for filename in os.listdir(dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            getText(filename)


main('scans')