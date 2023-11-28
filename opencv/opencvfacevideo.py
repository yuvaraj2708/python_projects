import cv2
import dlib

def load_reference_image(reference_image_path):
    # Load the reference image using OpenCV
    reference_image = cv2.imread(reference_image_path)
    # Convert to grayscale for dlib face detection
    reference_gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)
    return reference_gray

def find_faces(reference_gray, video_path):
    # Create a face detector and load the pre-trained model
    face_detector = dlib.get_frontal_face_detector()

    # Initialize the video capture
    cap = cv2.VideoCapture(video_path)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to grayscale for face detection
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Use the face detector on the current frame
        face_rects = face_detector(frame_gray)

        for rect in face_rects:
            # Draw a rectangle around the detected face
            x, y, w, h = rect.left(), rect.top(), rect.width(), rect.height()
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the frame with detected faces
        cv2.imshow('Video', frame)

        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Replace 'reference_image.jpg' with the path to your reference image
    reference_image_path = 'reference_image.jpg'

    # Replace 'video.mp4' with the path to your video file
    video_path = 'video.mp4'

    reference_gray = load_reference_image(reference_image_path)
    find_faces(reference_gray, video_path)
