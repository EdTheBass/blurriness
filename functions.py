from PIL import Image

def get_image():
    while True:
        img_input = input("Image: ")
        try:
            img = Image.open(rf"Pictures\{img_input}")
            break
        except FileNotFoundError:
            print("File not found.")
    
    return img, img_input
