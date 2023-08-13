# importing the necessary modules
import numpy as np
import cv2
import color

resized_image=np.zeros((720,512,3))

def call_back(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN or event==cv2.EVENT_RBUTTONDOWN:
        blue_val = resized_image[y, x, 0]
        green_val = resized_image[y, x, 1]
        red_val = resized_image[y, x, 2]
        lower_range = np.array([blue_val-30, green_val-30, red_val-30])
        upper_range = np.array([blue_val+30, green_val+30, red_val+30])
        mask = cv2.inRange(resized_image, lower_range, upper_range)
        # print(color.get_color(red_val, green_val, blue_val))
        ext_img=cv2.bitwise_and(resized_image,resized_image,mask=mask)
        cv2.imshow("choosen color portion",ext_img)


def extract_color(image):
    global resized_image
    resized_image=cv2.resize(image,(720,512))
    cv2.imshow("your_image",resized_image)
    cv2.setMouseCallback("your_image",call_back)
    cv2.waitKey(0)

if __name__=="__main__":
    input_image=cv2.imread("E:\\mem\\Trip media From Phanish\\New folder\\IMG20230430171451.jpg")
    resized_image=cv2.resize(input_image,(720,512))
    extract_color(resized_image)
