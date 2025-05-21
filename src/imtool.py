
import sys
import os
from PIL import Image, ImageFilter

def load_image(filename):
    return Image.open(os.path.join("..", "imgs", filename))

def save_image(img, original_name, suffix):
    name, ext = os.path.splitext(original_name)
    new_filename = f"{name}_{suffix}.jpg"
    img.save(os.path.join("..", "results", new_filename))
    print(f"Saved: {new_filename}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法: python imtool.py <檔名> <指令> [參數]")
        sys.exit(1)

    filename = sys.argv[1]
    option = sys.argv[2]

    img = load_image(filename)

    if option == "-resize":
        scale = float(sys.argv[3])
        new_size = (int(img.width * scale), int(img.height * scale))
        img = img.resize(new_size)
        save_image(img, filename, "resized")

    elif option == "-VFlip":
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        save_image(img, filename, "VFlip")

    elif option == "-HFlip":
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        save_image(img, filename, "HFlip")

    elif option == "-R90":
        img = img.rotate(-90, expand=True)
        save_image(img, filename, "R90")

    elif option == "-R180":
        img = img.rotate(180, expand=True)
        save_image(img, filename, "R180")

    elif option == "-R270":
        img = img.rotate(-270, expand=True)
        save_image(img, filename, "R270")

    elif option == "-thumbnail":
        width, height = int(sys.argv[3]), int(sys.argv[4])
        img.thumbnail((width, height))
        save_image(img, filename, "thumbnail")

    elif option == "-BLUR":
        img = img.filter(ImageFilter.BLUR)
        save_image(img, filename, "BLUR")

    elif option == "-CONTOUR":
        img = img.filter(ImageFilter.CONTOUR)
        save_image(img, filename, "CONTOUR")

    elif option == "-DETAIL":
        img = img.filter(ImageFilter.DETAIL)
        save_image(img, filename, "DETAIL")

    elif option == "-EDGE_ENHANCE":
        img = img.filter(ImageFilter.EDGE_ENHANCE)
        save_image(img, filename, "EDGE_ENHANCE")

    elif option == "-EDGE_ENHANCE_MORE":
        img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        save_image(img, filename, "EDGE_ENHANCE_MORE")

    elif option == "-EMBOSS":
        img = img.filter(ImageFilter.EMBOSS)
        save_image(img, filename, "EMBOSS")

    elif option == "-SHARPEN":
        img = img.filter(ImageFilter.SHARPEN)
        save_image(img, filename, "SHARPEN")

    elif option == "-SMOOTH":
        img = img.filter(ImageFilter.SMOOTH)
        save_image(img, filename, "SMOOTH")

    elif option == "-SMOOTH_MORE":
        img = img.filter(ImageFilter.SMOOTH_MORE)
        save_image(img, filename, "SMOOTH_MORE")

    elif option == "-FIND_EDGES":
        img = img.filter(ImageFilter.FIND_EDGES)
        save_image(img, filename, "FIND_EDGES")

    else:
        print("不支援的操作")
