#importing necessary modules
import cv2
import numpy as np
import color

resized_image=np.zeros((720,512))

def display_color(res_img,c,x,y,b,g,r):
    cv2.putText(res_img,"hjhj",(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(int(b),int(g),int(r)),5)
def call_back(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN or event==cv2.EVENT_RBUTTONDOWN:
        blue_val=resized_image[y,x,0]
        green_val=resized_image[y,x,1]
        red_val=resized_image[y,x,2]
        res_img = np.zeros((512, 512, 3), np.uint8)
        res_img[:]=[blue_val,green_val,red_val]
        color_rec=color.get_color(red_val, green_val, blue_val)
        cv2.imshow("Chosen color",res_img)
        display_color(res_img,color_rec, x, y, 0,0,0)

def detect_color(image):
    global resized_image
    resized_image = cv2.resize(image, (720, 512))
    cv2.imshow("your_image",resized_image)
    cv2.setMouseCallback("your_image",call_back)
    cv2.waitKey(0)


if __name__=="__main__":
# Reading the input image
    input_image=cv2.imread("E:\\mem\\Trip media from Murali\\IMG20230502121907.jpg")
#     resized_image=cv2.resize(input_image,(720,512))
#     detect_color(resized_image)
    detect_color(input_image)