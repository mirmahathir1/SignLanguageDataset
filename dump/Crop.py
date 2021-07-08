# annotate.py create folder 'rawvideos' and 'frames' where frames will contain x1,x2,y1,y2 coordinates of each video
# on a same named file ask whether the annotations already done should be done again read each video from rawvideo if
# the annotation of video doesn't exit or the annotations needed to be done all over again read a frame from the
# video using matplotlib click and mark the upper, lower, left and right bound generate annotation


# crop.py
# create folder 'croppedvideo'
# ask whether the coppings already done should be done again
# read each video from raw video
# if the annotation of video doesn't exit or the annotations needed to be done all over again
# crop the video and save to 'croppedvideo'


# In[1]:
import matplotlib.pyplot as plt

import moviepy.editor as mpy
from moviepy.video.fx.all import crop
import cv2


def crop_video_frame(video_path, x_top, y_top, x_bottom, y_bottom):
    clip = mpy.VideoFileClip(video_path)
    (w, h) = clip.size
    # cropped_clip = crop(clip, width=w / 3, height=(2 * h) / 3, x_center=w / 6, y_center=(h / 2) + 100)
    cropped_clip = crop(clip, width=int(x_bottom - x_top), height=int(y_bottom - y_top),
                        x_center=int((x_bottom + x_top) / 2), y_center=int((y_bottom + y_top) / 2))
    cropped_clip.write_videofile('cropped.mp4', audio_codec='aac')


def get_sample_frame_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(length)
    cap.set(1, int(length / 2))
    ret, frame = cap.read()
    return frame


def get_coordinates(image):
    """
    Show the frame, draw a rectangular selection box and close the window to get the coordinates
    """
    from matplotlib.widgets import RectangleSelector
    x1 = x2 = y1 = y2 = 0

    def line_select_callback(eclick, erelease):

        nonlocal x1, x2, y1, y2
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata
        # print("(%3.2f, %3.2f) --> (%3.2f, %3.2f)" % (x1, y1, x2, y2))
        # print(" The button you used were: %s %s" % (eclick.button, erelease.button))

    def toggle_selector(event):
        # print(' Key pressed.')
        if event.key in ['Q', 'q'] and toggle_selector.RS.active:
            # print(' RectangleSelector deactivated.')
            toggle_selector.RS.set_active(False)
        if event.key in ['A', 'a'] and not toggle_selector.RS.active:
            # print(' RectangleSelector activated.')
            toggle_selector.RS.set_active(True)

    fig, current_ax = plt.subplots()  # make a new plotting range

    plt.imshow(image)

    # print("\n      click  -->  release")

    # drawtype is 'box' or 'line' or 'none'
    toggle_selector.RS = RectangleSelector(current_ax, line_select_callback,
                                           drawtype='box', useblit=True,
                                           button=[1, 3],  # don't use middle button
                                           minspanx=5, minspany=5,
                                           spancoords='pixels',
                                           interactive=True)
    plt.connect('key_press_event', toggle_selector)
    plt.show()
    return x1, y1, x2, y2


video_name = "sample.mp4"
frame = get_sample_frame_from_video(video_name)
selection = get_coordinates(frame)
crop_video_frame(video_name, selection[0], selection[1], selection[2], selection[3])
