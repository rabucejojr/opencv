import os
import cv2

# Take input of the person name
name = input("Enter name:  ")
img_counter = 0
# Create the videocapture object
cap = cv2.VideoCapture(0)

while True:
    # Read each frame
    success, frame = cap.read()
    # Show the output
    cv2.imshow("Frame", frame)
    k = cv2.waitKey(1)
    if k == ord('c'):
        path = r'C:\Users\programmer\Desktop\OPENCV Python/images'
        img_name = name+"{}.png".format(img_counter)
        cv2.imwrite(os.path.join(path, img_name), frame)
        print("Image Saved- ", img_name)
        break
    elif k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
