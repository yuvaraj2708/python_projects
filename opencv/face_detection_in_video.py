import cv2

# Load the reference image
reference_image = cv2.imread("image1.jpeg", cv2.IMREAD_GRAYSCALE)

# Open video file or webcam stream
video_path = "whats.mp4"
video_capture = cv2.VideoCapture(video_path)

# Get the width and height of the reference image
reference_height, reference_width = reference_image.shape

# Define the threshold for matching
threshold = 0.8

while True:
    # Read the current frame from the video
    ret, frame = video_capture.read()

    if not ret:
        break

    # Convert the current frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform template matching
    result = cv2.matchTemplate(gray_frame, reference_image, cv2.TM_CCOEFF_NORMED)

    # Find the location of the best match in the result
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # If the best match exceeds the threshold, consider it a match
    if max_val >= threshold:
        # Get the top-left and bottom-right corners of the bounding box
        top_left = max_loc
        bottom_right = (top_left[0] + reference_width, top_left[1] + reference_height)

        # Draw a rectangle around the matched region
        cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow("Video", frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the windows
video_capture.release()
cv2.destroyAllWindows()
