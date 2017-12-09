from PIL import Image

ASCII_CHARS = ["$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'.", " .:-=+*#%@", "@%#*+=-;:. "]
#First set is detailed, second two are flipped versions of each other.
CHARSET = 0
WIDTH = 120

def greyscale(img):
    return img.convert("L")

def resize(img, new_width):
    size = img.size
    ratio = size[1]/size[0]
    new_height = int(ratio * new_width)
    n_img = img.resize((new_width, new_height))
    return n_img

def map_chars(img, chars):
    print(chars)
    pixels = list(img.getdata())
    n_pixels = [chars[int(pix/(256 / len(chars)))] for pix in pixels]
    n_pixels = "".join(n_pixels)
    return n_pixels

def ASCIIfy_image(path, chars, width=150):
    img = Image.open(path)
    img = greyscale(resize(img, width))
    chars = map_chars(img, chars)
    n_img = [chars[index: index + width] for index in range(0, len(chars), width)]
    return "\n".join(n_img)
    

print("###############################")
print("#        THE ASCIIFIER        #")
print("###############################")
print("Welcome to the ASCIIfier.")
print("Use this program to convert images to ASCII.")
print("Type '$help' for more information.")
print("Type a filename to begin.")
print()
while True:
    command = input(">")    
    if command[0] == "$":
        command = command.split(" ")
        if command[0] == "$width":
            if int(command[1]):
               WIDTH = int(command[1])
               print("Width has been set to", command[1] + ".")
            else:
                print("Invalid command")
        elif command[0] == "$charset":
            if len(ASCII_CHARS) - 1 >= int(command[1]):
                CHARSET = int(command[1])
                print("Charset has been set to", command[1] + ".")
            else:
                print("No such charset found.")
        elif command[0] == "$help":
            print("ASCIIfier HELP:")
            print("Enter the name of an image file (plus extension) and then press 'Enter.'")
            print("The program will output your ASCIIfied image.")
            print("Enter '$width ' and then a number to change the default width.")
            print("Enter '$charset ' and then a number to change the default charset.")     
        else:
            print("Invalid command.")
    else:
        try:
            print(ASCIIfy_image(command, ASCII_CHARS[CHARSET], WIDTH))
            print()
            print("Enter another filename to convert another image.")
        except:
            print("Could not convert", command +".", "Sorry.")
    print()
