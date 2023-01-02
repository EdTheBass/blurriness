from functions import *
from time import time

DEPTH = 10

img, inp = get_image()

pixels = img.load()
num_pixels = list(img.size)
img_x = num_pixels[0]
img_y = num_pixels[1]


def generate_pixels(x, y):
    pixels = []
    min_x = max(x-DEPTH, 0)
    max_x = min(x+DEPTH+1, img_x)
    min_y = max(y-DEPTH, 0)
    max_y = min(y+DEPTH+1, img_y)
    for i in range(min_x, max_x):
        for j in range(min_y, max_y):
            pixels.append(list(img.getpixel((i, j))))
    return pixels

def average_pixels(pixels):
    total_rgb = [0, 0, 0]
    for p in pixels:
        r1,g1,b1 = total_rgb
        try:
            r2,g2,b2 = p
        except ValueError:
            r2,g2,b2,_ = p
        total_rgb = [r1+r2, g1+g2, b1+b2]
        
    r,g,b = total_rgb
    return [r//len(pixels), g//len(pixels), b//len(pixels)]

def pixel_operation(x, y):
    ps = generate_pixels(x, y)
    new_pixel = average_pixels(ps)

    return new_pixel


denominator = img_x * img_y
start = time()
for x in range(img_x):
    for y in range(img_y):
        rgb = pixel_operation(x, y)

        pixels[x, y] = tuple(rgb)

    numerator = (x+1) * img_y
    elapsed_time = time() - start
    idfk = numerator/denominator
    print(f"{idfk*100:0.2f}%")

img.save(rf"Pictures\blurry {inp}")
print("Image Saved.")