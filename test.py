import cv2

# Initialize the camera
cam = cv2.VideoCapture(0)

# Start an infinite loop for real-time image processing
while True:
    # Read a frame from the camera
    status, photo = cam.read()
    
    # Perform image manipulation: cropping and copying
    photo[0:200, 0:150] = photo[100:300, 150:300]
    
    # Display the modified image
    cv2.imshow("myphoto", photo)
    
    # Check for the 'Enter' key press to exit the loop
    if cv2.waitKey(10) == 13:
        break

# Release the camera and close all windows
cv2.destroyAllWindows()
cam.release()