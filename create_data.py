import cv2
import numpy as np
import os



################## LOAD IMAGE ##################

image = 'image1'

original_image = cv2.imread(f'{image}.jpg')



################## ENHANCE IMAGE ##################

# Values
alpha = 1.2
beta = 0

# Increase contrast
enhanced_image = cv2.addWeighted(original_image, alpha, np.zeros(original_image.shape, original_image.dtype), 0, beta)



################## CROAP IMAGE ##################

# Define the pixel coordinates of the top-left and bottom-right corners
top_left_corner = (531, 240)
bottom_right_corner = (1200, 1436)

cropped_image = enhanced_image[top_left_corner[1]:bottom_right_corner[1], top_left_corner[0]:bottom_right_corner[0]]

cv2.imshow('Cropped Image', cropped_image)
cv2.waitKey(0)



################## CREATE CELLS ##################

# Create a folder for output cells
os.makedirs(image, exist_ok=True)

# Define the number of rows and columns for the grid
rows = 22
cols = 15

# Calculate the height and width of each cell
height, width, _ = cropped_image.shape
cell_height = height // rows
cell_width = width // cols


# Iterate through the rows and columns to crop the image into cells
for i in range(rows):

    for j in range(cols):

        # Calculate the coordinates of the top-left and bottom-right corners of the cell
        y_start = i * cell_height
        y_end = (i + 1) * cell_height
        x_start = j * cell_width
        x_end = (j + 1) * cell_width

        # Crop the cell from the cropped image
        cell = cropped_image[y_start:y_end, x_start:x_end]

        # Define the filename for the cell
        cell_filename = f'{image}/{i}_{j}.jpg'

        # Save the cell
        cv2.imwrite(cell_filename, cell)

cv2.waitKey(0)
cv2.destroyAllWindows()