from PIL import Image


def convert_to_display_array(img) -> list:
    width, height = img.size
    display_array = []

    for i in range(0, height, 8):
        row_bytes = []
        for j in range(width):
            byte = 0
            for k in range(8):
                try:
                    pixel = img.getpixel((j, i + k))
                except IndexError:
                    pixel = 0
                if pixel == 0:
                    byte |= 1 << k
            row_bytes.append(byte)
        display_array.append(row_bytes)

    return display_array


def to_hex_string(num):
    hex_string = hex(num)
    return str(hex_string.upper())


def beauty_print(arr: list, double_arr: bool):
    if double_arr:
        print("{")
        for i in arr:
            print("\t{", end="")
            print(*i, sep=", ", end="")
            print("}", end=",\n")
        print("}")
    else:
        print("{")
        for i in arr:
            dd = []
            for k in i:
                dd.append(to_hex_string(k))
            print(*dd, sep=", ", end="")
            print(",")
        print("}")
