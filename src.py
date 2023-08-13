#importing the necessary modules
import cv2
import numpy as np
import image_color
import vid_color
import extract_color

print('''
    Choose the functionality:
        1--> Detect the color in an image.
        2--> Detect the color of an object placed in front of the camera.
        3--> Extract the color portions of particular color from the image
''')

option = int(input("Choose your option"))

input_image=cv2.imread("E:\\mem\\Trip media from Murali\\IMG20230502121907.jpg")

if option == 1:
    image_color.detect_color(input_image)
elif option==2:
    vid_color.capture()
else:
    extract_color.extract_color(input_image)