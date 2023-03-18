import os
import cv2

# Function to extract frames
def FrameCapture(path):

    # Path to video file
    vidObj = cv2.VideoCapture(path)

    # Used as counter variable
    count = 0
    frame = 1

    # checks whether frames were extracted
    success = 1

    while success:

        # vidObj object calls read
        # function extract frames
        success, image = vidObj.read()

        # Saves the frames with frame-count
        cv2.imwrite("Capt Images/frame%d.jpg" % frame, image)

        frame += 1
        count += 30
        vidObj.set(1, count)


# Driver Code
if __name__ == '__main__':

    # Calling the function
    FrameCapture("Data/train1.mp4")

#%%
