import cv2
import numpy as np
from scipy.signal import fftconvolve

# Open the default camera (device index 0)
cap = cv2.VideoCapture(0)

#laplacian matrix for edge detection
kernel = np.array([
					[ -1, 0, -1],
					[  0, 4,  0],
					[ -1, 0, -1]
                   ])/9    

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
else:
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        frame1 = np.array(frame[:,:,0])
        frame2 = np.array(frame[:,:,1])
        frame3 = np.array(frame[:,:,2])
        

        # If frame is not read successfully, break the loop
        if not ret:
            print("Error: Could not read frame.")
            break

        # Display the frame
        cv2.namedWindow('Red Stream', cv2.WINDOW_NORMAL)
        #convolve kernel and image arrays
        frameskt = fftconvolve(frame1, kernel)
        cv2.imshow('Red Stream', frameskt)
        
        #green channel
        cv2.namedWindow('Green Stream', cv2.WINDOW_NORMAL)
        #convolve kernel and image arrays
        frameskt2 = fftconvolve(frame2, kernel)
        cv2.imshow('Green Stream', frameskt2)
        
        #blue channel
        cv2.namedWindow('Blue Stream', cv2.WINDOW_NORMAL)
        #convolve kernel and image arrays
        frameskt3 = fftconvolve(frame3, kernel)
        cv2.imshow('Blue Stream', frameskt3)
        
        # Get frame rate information
        # You can replace 5 with CAP_PROP_FPS as well, they are enumerations
        fps = cap.get(5)
        print('Frames per second : ', fps,'FPS')
        # Get frame count
        # You can replace 7 with CAP_PROP_FRAME_COUNT as well, they are enumerations
        frame_count = cap.get(7)
        print('Frame count : ', frame_count)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and destroy all windows
    cap.release()
    cv2.destroyAllWindows()
