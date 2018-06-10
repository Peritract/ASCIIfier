from PIL import Image

ASCII_CHARS = [" .:-=+*#%@", "@%#*+=-;:. ", "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'."]
#1 and 2 are flipped versions of each other.
CHARSET = 0
WIDTH = 120
ASCII_IMG = []

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

def save_img(img, filename):
    file = open(filename + ".txt", "w")
    file.write(img)
    print("File saved successfully.")

def help():
    print("ASCIIfier HELP:")
    print("Enter the name of an image file (plus extension) and then press 'Enter.'")
    print("The program will output your ASCIIfied image.")
    print("Enter '$width ' and then a number to change the default width.")
    print("Enter '$charset ' and then a number to change the default charset.")
    print("Enter '$save ' and then a name to save the most recent image.")

def main():
    global ASCII_IMG #I know global variables are frowned upon, but given the small size and limited
    #purpose of this program, I think it's excusable in the 3 places they appear.
    
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
            if len(command) > 1 and can_int(command[1]):
                if command[0] == "$width":
                    set_width(int(command[1]))
                elif command[0] == "$charset":
                    set_charset(int(command[1]))
            elif command[0] == "$save":
                if len(command) > 1 and len(ASCII_IMG) > 0:
                    save_img(ASCII_IMG, command[1])
                elif len(ASCII_IMG) == 0:
                    print("ERROR: No image to save.")
                elif len(command) == 1:
                    print("ERROR: No filename provided.")
            elif command[0] == "$help":
                help()    
            else:
                print("Invalid command.")
        else:
            try:
                ASCII_IMG = ASCIIfy_image(command, ASCII_CHARS[CHARSET], WIDTH)
                print(ASCII_IMG)
            except:
                print("ERROR: Unable to convert", command)
        print()

if __name__ == "__main__":
    main()
