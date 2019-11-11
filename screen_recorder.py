import cv2
import numpy as np
from time import perf_counter
import pyautogui

### IMPORTANT!! DOES NOT RECORD AUDIO.

# display screen resolution, get it from your OS settings
SCREEN_SIZE = (1920, 1080)

# define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")

# create the video write object
out = cv2.VideoWriter("output.avi", fourcc, 25.0, (SCREEN_SIZE))
# filename, codec, fps to record, screen size
try:
    while True:
        # make a screenshot
        img = pyautogui.screenshot()
        # convert these pixels to a proper numpy array to work with OpenCV
        frame = np.array(img)
        # convert colors from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # write the frame
        out.write(frame)
        # show the frame
        cv2.imshow("screenshot", frame)
        # if the user clicks q, it exits
        if cv2.waitKey(1) == ord("q"):
            break
except:
    KeyboardInterrupt
# make sure everything is closed when exited
cv2.destroyAllWindows()
out.release()