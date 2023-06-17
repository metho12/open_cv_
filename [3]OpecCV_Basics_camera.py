# import the required packages
import cv2

clicked = False

# create a function to monitor the mous click
def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP: # when you press the left mouse button.
        clicked = True


# Initialize the camera capture object. 0 means camera
cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('Camera Frame')
cv2.setMouseCallback('Camera Frame', onMouse)

print('Showing camera feed. Click window or press any key to stop.')
success, frame = cameraCapture.read()
while cv2.waitKey(1) == -1 and not clicked:
    if frame is not None:
        cv2.imshow('Camera Frame', frame)
    success, frame = cameraCapture.read()

cv2.destroyWindow('MyWindow')