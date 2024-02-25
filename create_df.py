import pandas as pd


initials = 'ds'


################## CREATE DATAFRAME ##################

# Create an empty list to store data
data = []

# Initialize counters
image = 1
i = 0
j = 0

# Loop through each letter in text.txt
with open('text.txt', 'r') as file:
    data = []
    
    for letter in file.read().strip():
        data.append({'letter': letter, 'image': f'images/{initials}{image}-{i}_{j}.jpg'})


        # Increment i every 14 iterations
        if (j + 1) % 15 == 0:
            i += 1

            # Reset i when it reaches 22
            if i == 22:
                image += 1
                i = 0

        # Increment j every iteration, and restart j to 0 every time it reaches 14
        j = (j + 1) % 15

# Create DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Save the DataFrame as a CSV file
df.to_csv(f'{initials}_df.csv', index=False)