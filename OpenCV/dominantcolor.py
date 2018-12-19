from PIL import Image

def dominant(img):
    img.show()
    w, h = img.size
    pixels = img.getcolors(w * h)
    pixels.sort()
    #print(pixels)
    most_frequent_pixel = pixels[0] 
    for count, colour in pixels:
        if count > most_frequent_pixel[0]:
            most_frequent_pixel = (count, colour)
    #compare("Most Common", img, most_frequent_pixel[1])
    print("True")
    print(pixels[-1])
