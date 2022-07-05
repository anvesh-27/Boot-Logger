from datetime import datetime
import cv2

now = datetime.now()
date_time = now.strftime("%d %B %Y %I-%M-%S %p")

def Create_Boot_logs():
    
    f = open("Boot_logs.txt", "a")
    f.write(f"System booted at {date_time}\n")

    f.close

def Capture_User_image():

    cam_port = 0 #Your camera port may differ, set it accordingly.
    cam = cv2.VideoCapture(cam_port)

    result, image = cam.read()
    
    if result:
    
        cv2.imshow("User image", image)
    
        cv2.imwrite(f"{date_time}.png", image)

        cv2.destroyWindow("User image")

    else:
        print("No image detected. Please! try again")

Create_Boot_logs()
Capture_User_image()