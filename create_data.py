import cv2
import numpy as np
import os



################## LOAD IMAGE ##################

image = 'image2'

original_image = cv2.imread(f'{image}.jpg')



################## ENHANCE IMAGE ##################

# Values
alpha = 1.2
beta = 0

# Increase contrast
enhanced_image = cv2.addWeighted(original_image, alpha, np.zeros(original_image.shape, original_image.dtype), 0, beta)



################## CREATE CELLS ##################

# Create a folder for output cells
os.makedirs(image, exist_ok=True)

# Top left corner. 
# Odd Pages: (531, 241)
# Even Page: (515, 241)
top_left_x = 515
top_left_y = 241

# Values
cols = 15
rows = 22
cell_size = 32
margin_x = 13
margin_y = 23

# Iterate through the rows and columns to crop the image into cells
for i in range(rows):

    for j in range(cols):

        # Calculate the coordinates of the top-left and bottom-right corners of the cell with margin
        x_start = j * (cell_size + margin_x) + top_left_x
        x_end = x_start + cell_size
        y_start = i * (cell_size + margin_y) + top_left_y
        y_end = y_start + cell_size

        # Crop the cell from the cropped image
        cell = enhanced_image[y_start:y_end, x_start:x_end]

        # Save the cell
        cv2.imwrite(f'{image}/{i}_{j}.jpg', cell)