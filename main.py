# This is a sample Python script.
from MT12864J.image import *
from MT12864J.transform import *
import cv2


WIDTH = 30
HEIGHT = 30
IMG_PATH = 'img_2.jpg'
SAVE_IMG_PATH = 'image_res.jpg'
THRESHOLD_VALUE = 210


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    img = open_image(IMG_PATH)
    # img = resize_image(img, WIDTH, HEIGHT)
    img = convert_image(img)
    img = threshold_iamge(THRESHOLD_VALUE, img)
    show_image(img)
    save_image(img, SAVE_IMG_PATH)
    beauty_print(convert_to_display_array(img), double_arr=True)
