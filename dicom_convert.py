import os
import pydicom
from PIL import Image
import numpy as np

# Set the path to the folder containing the JPG images
folder_path = r'C:\Users\Admin\Pictures\Saved Pictures'

# Get a list of all the JPG images in the folder
jpg_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]

# Create an empty list to store the pixel arrays of each image
image_arrays = []

# Set the desired width and height for the resized images
target_width = 1920
target_height = 1080

# Loop through each JPG image, resize, and convert them to numpy arrays
for jpg_file in jpg_files:
    # Load the JPG image
    image = Image.open(os.path.join(folder_path, jpg_file))

    # Resize the image to the target width and height
    image = image.resize((target_width, target_height))

    # Convert the image to a numpy array
    image_array = np.array(image)
    image_arrays.append(image_array)

# Create a new DICOM dataset
ds = pydicom.Dataset()

# Set the necessary DICOM attributes
ds.Rows, ds.Columns, _ = image_arrays[0].shape

ds.BitsAllocated = 8
ds.BitsStored = 8
ds.HighBit = 7
ds.PixelRepresentation = 0  # Unsigned integer
ds.SamplesPerPixel = 3  # RGB image
ds.PhotometricInterpretation = "RGB"
ds.NumberOfFrames = len(image_arrays)

# Create an empty list to store the pixel data of each frame
pixel_data_frames = []

# Rescale the pixel values if necessary and add them to the pixel data frames
for image_array in image_arrays:
    if np.amax(image_array) > 255:
        image_array = image_array * (255 / np.amax(image_array))
    image_array = image_array.astype(np.uint8)
    pixel_data_frames.append(image_array.tobytes())

# Set the pixel data to the concatenated frames
ds.PixelData = b''.join(pixel_data_frames)

# Set the transfer syntax for lossless compression
ds.file_meta = pydicom.Dataset()
ds.file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRLittleEndian  # Use Explicit VR Little Endian compression

# Save the DICOM file
output_path = os.path.join(folder_path, 'combined_image.dcm')
ds.save_as(output_path)
