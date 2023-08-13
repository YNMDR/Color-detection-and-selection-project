# importing necessary modules
import numpy as np
import cv2
import color

vid_frame=np.zeros((720,512))
def call_back(event,x,y,flags,params):
    if event==cv2.EVENT_MOUSEMOVE:
        blue_val=vid_frame[y,x,0]
        green_val=vid_frame[y,x,1]
        red_val=vid_frame[y,x,2]
        print(color.get_color(red_val,green_val,blue_val))
        res_img = np.zeros((512, 512, 3), np.uint8)
        res_img[:]=[blue_val,green_val,red_val]
        cv2.imshow("Choosen color",res_img)

def capture():
    # To read the video
    vid=cv2.VideoCapture(0)
    vid.set(3,720)
    vid.set(4,512)

    if not vid.isOpened():
        vid.open()
    while True:
        global vid_frame
        suc,vid_frame=vid.read()
        if suc:
            cv2.imshow("Camera",vid_frame)
            cv2.setMouseCallback("Camera",call_back)
            k=cv2.waitKey(1)
            if k==65:
                break
        else:
            print("Failed to read the frame")
            break
