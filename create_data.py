import cv2
import numpy as np
import os



################## LOAD IMAGE ##################

image = 'image3'
original_image = cv2.imread(f'{image}.jpg')



################## BINARIZE IMAGE ##################

# Convert the image to grayscale
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
inverted_gray_image = 255 - gray_image

# Apply binary thresholding
_, binary_image = cv2.threshold(inverted_gray_image, 12, 255, cv2.THRESH_BINARY)

#cv2.imshow('Binary Image', binary_image)



################## FIND LIMITS ##################

threshold = 60000

# Calculate the row-wise sum of the binary image
row_sum = np.sum(binary_image, axis=1)

# Calculate the column-wise sum of the binary image
column_sum = np.sum(binary_image, axis=0)

# Identify horizontal lines by finding rows where the row sum exceeds the threshold
horizontal_lines = np.where(row_sum > threshold)[0]

# Identify vertical lines by finding columns where the column sum exceeds the threshold
vertical_lines = np.where(column_sum > threshold)[0]

# Extract the indices of the first and last horizontal lines
first_horizontal_line = horizontal_lines[0]
last_horizontal_line = horizontal_lines[-1]

# Extract the indices of the first and last vertical lines
first_vertical_line = vertical_lines[0]
last_vertical_line = vertical_lines[-1]

# Draw Lines
cv2.line(original_image, (0, first_horizontal_line), (original_image.shape[1], first_horizontal_line), (0, 0, 255), 2)
cv2.line(original_image, (0, last_horizontal_line), (original_image.shape[1], last_horizontal_line), (0, 0, 255), 2)
cv2.line(original_image, (first_vertical_line, 0), (first_vertical_line, original_image.shape[0]), (0, 0, 255), 2)
cv2.line(original_image, (last_vertical_line, 0), (last_vertical_line, original_image.shape[0]), (0, 0, 255), 2)

cv2.imshow('Limits', original_image)



################## CROP IMAGE ##################

# Crop the image within the detected lines
cropped_image = gray_image[first_horizontal_line:last_horizontal_line, first_vertical_line:last_vertical_line]

#cv2.imshow('Cropped Image', cropped_image)



################## INCREASE CONTRAST ##################

# Values
alpha = 1.1
beta = 0

# Increase contrast
enhanced_image = cv2.addWeighted(cropped_image, alpha, np.zeros(cropped_image.shape, cropped_image.dtype), 0, beta)



################## CREATE CELLS ##################

# Create a folder for output cells
os.makedirs(image, exist_ok=True)

# 36 x 36
cell_size = 36

# Get the height and width of the cropped image
enhanced_image_height, enhanced_image_width = enhanced_image.shape

margin_x = (enhanced_image_width - cell_size * 15) / 14
margin_y = (enhanced_image_height - cell_size * 22) / 21

#print(margin_x)
#print(margin_y)


for i in range(22):

    for j in range(15):

        # Calculate the coordinates of the top-left and bottom-right corners of the cell with margin
        x_start = int(j * (cell_size + margin_x))
        x_end = int(x_start + cell_size)
        y_start = int(i * (cell_size + margin_y))
        y_end = int(y_start + cell_size)

        # Crop the cell from the cropped image
        cell = enhanced_image[y_start:y_end, x_start:x_end]

        # Save the cell
        cv2.imwrite(f'{image}/{i}_{j}.jpg', cell)


cv2.waitKey(0)
cv2.destroyAllWindows()