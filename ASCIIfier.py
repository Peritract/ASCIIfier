from PIL import Image

ASCII_CHARS = [" .:-=+*#%@", "@%#*+=-;:. ", "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'."]
#1 and 2 are flipped versions of each other.
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

def set_width(width):
    global WIDTH
    WIDTH = int(width)
    print("Width has been set to", str(width) + ".")

def set_charset(num):
    global CHARSET
    if len(ASCII_CHARS) - 1 >= num:
        CHARSET = num
        print("Charset has been set to", str(num) + ".")
    else:
        print("No such charset found.")

def can_int(x):
    #helper function - checks if something can be an integer
    try:
        int(x)
        return True
    except:
        return False

def help():
    print("ASCIIfier HELP:")
    print("Enter the name of an image file (plus extension) and then press 'Enter.'")
    print("The program will output your ASCIIfied image.")
    print("Enter '$width ' and then a number to change the default width.")
    print("Enter '$charset ' and then a number to change the default charset.") 

def main():
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
            print(command[1])
            if len(command) > 1 and can_int(command[1]):
                if command[0] == "$width":
                    set_width(int(command[1]))
                elif command[0] == "$charset":
                    set_charset(int(command[1]))
            elif command[0] == "$help":
                help()    
            else:
                print("Invalid command.")
        else:
            try:
                print(ASCIIfy_image(command, ASCII_CHARS[CHARSET], WIDTH))
            except:
                print("ERROR: Unable to convert", command)
        print()

if __name__ == "__main__":
    main()
