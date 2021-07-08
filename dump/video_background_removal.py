import cv2
import numpy as np

cap = cv2.VideoCapture("cropped_videos/Do not wreck this now Van-Tam pleads 🔴 @BBC News live - BBC.mp4")

if not cap.isOpened():
    print("Unable to read camera feed")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter('outpy.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

while True:
    ret, frame = cap.read()

    if ret:
        height, width = frame.shape[:2]

        # Create a mask holder
        mask = np.zeros(frame.shape[:2], np.uint8)

        # Grab Cut the object
        bgdModel = np.zeros((1, 65), np.float64)
        fgdModel = np.zeros((1, 65), np.float64)

        # Hard Coding the Rect The object must lie within this rect.
        rect = (int(width / 5.0), int(height / 6.0), int(3 * width / 5.0), int(5 * height / 6.0))
        cv2.grabCut(frame, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
        mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
        img1 = frame * mask[:, :, np.newaxis]

        # Get the background
        background = frame - img1

        # Change all pixels in the background that are not black to white
        background[np.where((background > [0, 0, 0]).all(axis=2))] = [255, 255, 255]

        # Add the background and the image
        final = background + img1

        out.write(final)

        # cv2.imshow('frame', frame)

        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    else:
        break

cap.release()
out.release()

cv2.destroyAllWindows()
