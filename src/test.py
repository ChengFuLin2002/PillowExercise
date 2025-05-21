
import os
import sys
from PIL import Image

def jpg2png(origName, newImgName):
    try:
        im = Image.open(origName)
        im.save(newImgName, 'png')
        print(f"Converted: {origName} -> {newImgName}")
    except FileNotFoundError as fnfe:
        print(fnfe)

def png2jpg(origName, newImgName):
    try:
        im = Image.open(origName)
        im = im.convert('RGB')  # 確保 PNG 可儲存為 JPEG
        im.save(newImgName, 'jpeg')
        print(f"Converted: {origName} -> {newImgName}")
    except FileNotFoundError as fnfe:
        print(fnfe)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("請使用 python test.py -jpg2png 或 -png2jpg")
        sys.exit(1)

    input_dir = os.path.join("..", "imgs")
    output_dir = os.path.join("..", "results")
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        filepath = os.path.join(input_dir, filename)
        name, ext = os.path.splitext(filename)
        ext = ext.lower()

        if sys.argv[1] == "-jpg2png" and ext in ['.jpg', '.jpeg']:
            output_path = os.path.join(output_dir, name + '.png')
            jpg2png(filepath, output_path)

        elif sys.argv[1] == "-png2jpg" and ext == '.png':
            output_path = os.path.join(output_dir, name + '.jpg')
            png2jpg(filepath, output_path)
