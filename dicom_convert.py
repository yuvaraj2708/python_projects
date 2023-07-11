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

# Loop through each JPG image and convert them to numpy arrays
for jpg_file in jpg_files:
    # Load the JPG image
    image = Image.open(os.path.join(folder_path, jpg_file))

    # Convert the image to a numpy array
    image_array = np.array(image)
    image_arrays.append(image_array)

# Create a new DICOM dataset
ds = pydicom.Dataset()

# Add specific DICOM tags
ds.add_new(pydicom.tag.Tag(0x0008, 0x0005), 'CS', 'ISO_IR 100')  # Specific Character Set
ds.add_new(pydicom.tag.Tag(0x0008, 0x0020), 'DA', '20050927')    # Study Date
ds.add_new(pydicom.tag.Tag(0x0008, 0x0030), 'TM', '185646')      # Study Time
ds.add_new(pydicom.tag.Tag(0x0008, 0x0050), 'SH', 'A10011234814')  # Accession Number
ds.add_new(pydicom.tag.Tag(0x0008, 0x0090), 'PN', 'CHIR-PED^CHIR-PE')  # Referring Physician's Name
ds.add_new(pydicom.tag.Tag(0x0008, 0x0096), 'PN', 'Referring Physician Name Ideographic')  # Referring Physician's Name Ideographic
ds.add_new(pydicom.tag.Tag(0x0008, 0x0097), 'PN', 'Referring Physician Name Phonetic')  # Referring Physician's Name Phonetic
ds.add_new(pydicom.tag.Tag(0x0008, 0x1030), 'LO', 'CT2 tête, face, sinus')  # Study Description
ds.add_new(pydicom.tag.Tag(0x0008, 0x1032), 'SQ', [])  # Procedure Code Sequence

# Create Procedure Code Sequence
sequence_item = pydicom.Dataset()
ds.ProcedureCodeSequence = [sequence_item]

# Add Procedure Code attributes
sequence_item.CodeValue = 'CTTETE'
sequence_item.CodingSchemeDesignator = 'XPLORE'
sequence_item.CodeMeaning = 'CT2 TÊTE, FACE, SINUS'

ds.add_new(pydicom.tag.Tag(0x0010, 0x1010), 'AS', '014Y')  # Patient's Age
ds.add_new(pydicom.tag.Tag(0x0020, 0x000D), 'UI', '2.16.840.1.113669.632.20.1211.10000098591')  # Study Instance UID
ds.add_new(pydicom.tag.Tag(0x0020, 0x0010), 'SH', '123456789')  # Study ID

# Set the necessary DICOM attributes
ds.PatientName = 'John Doe'
ds.PatientID = '12345'
ds.Modality = 'CT'
ds.SOPInstanceUID = pydicom.uid.generate_uid()
ds.StudyInstanceUID = pydicom.uid.generate_uid()
ds.SeriesInstanceUID = pydicom.uid.generate_uid()
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

# Set the transfer syntax attributes
ds.file_meta = pydicom.Dataset()
ds.file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRLittleEndian

# Save the DICOM file
output_path = os.path.join(folder_path, 'combined_image.dcm')
ds.save_as(output_path)
