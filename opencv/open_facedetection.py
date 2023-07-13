import cv2
import face_recognition
import glob

# Load the reference image for comparison
reference_image = cv2.imread("image1.jpeg")
reference_encoding = face_recognition.face_encodings(reference_image)[0]

# Path to the directory containing the images
directory_path = r"C:\Users\Admin\Desktop\imagecv\\"

# Retrieve all image file paths within the directory
image_paths = glob.glob(directory_path + "*.jpeg") + glob.glob(directory_path + "*.png")+glob.glob(directory_path + "*.jpg")+glob.glob(directory_path + "*.webp")

# Set the window size for display
window_width, window_height = 600, 400

# Create a window to display the images
cv2.namedWindow("Reference and Matching Images", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Reference and Matching Images", window_width * 2, window_height)

# Loop through each image for comparison
for image_path in image_paths:
    # Read the current image
    current_image = cv2.imread(image_path)
    
    # Convert the image to RGB format
    rgb_image = cv2.cvtColor(current_image, cv2.COLOR_BGR2RGB)
    
    # Encode the face in the current image
    current_encoding = face_recognition.face_encodings(rgb_image)[0]
    
    # Compare the current encoding with the reference encoding
    result = face_recognition.compare_faces([reference_encoding], current_encoding)
    
    # Check if the current image matches the reference image
    if result[0]:
        print(f"Found a matching image: {image_path}")
        
        # Resize the images to the desired dimensions
        reference_image_resized = cv2.resize(reference_image, (window_width, window_height))
        current_image_resized = cv2.resize(current_image, (window_width, window_height))
        
        # Concatenate the reference image and the matching image horizontally
        combined_image = cv2.hconcat([reference_image_resized, current_image_resized])
        
        # Display the concatenated image in the window
        cv2.imshow("Reference and Matching Images", combined_image)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        break