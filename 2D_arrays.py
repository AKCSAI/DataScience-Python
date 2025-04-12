# This script creates a 2D NumPy array from a list of baseball player data.
# Each sublist contains a player's height (in inches) and weight (in pounds).
# The script then prints:
# 1. The type of the created object (to confirm it's a NumPy array)
# 2. The shape of the array (i.e., number of rows and columns)

import numpy as np

# array[rows, columns]
# A list of baseball player data: [height, weight]
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D NumPy array from the baseball list
np_baseball = np.array(baseball)

# Print the type of np_baseball (should be <class 'numpy.ndarray'>)
print(type(np_baseball))

# Print the shape of np_baseball (rows, columns) → (4, 2)
print(np_baseball.shape)



# This script converts a list called 'baseball' into a NumPy array and performs the following:
# 1. Prints all player data from the 50th player onward
# 2. Extracts and prints the second column (e.g., player weights) for all players
# 3. Attempts to print the height of the 124th player (note: the slicing syntax is incorrect and needs fixing)

import numpy as np

np_baseball = np.array(baseball)
# Sample data: [height in inches, weight in pounds]
# Simulating a list of 130 players for indexing (at least up to 124)
baseball = [[180 + i % 10, 75 + i % 15] for i in range(130)]

# array[rows, columns]

# Print out the 50th row and beyond of np_baseball
print(np_baseball[49:,])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:, 1]
print(np_weight_lb)

# Print out height of 124th player (Incorrect slicing — fix below)
# print("124th player's height:", np_baseball[123:0])  # ❌ This doesn't work

# ✅ Correct version:
print("124th player's height:", np_baseball[123, 0])  # Correctly access the height of the 124th player



# This script creates a NumPy array containing height and weight data for 5 players.
# It then extracts only the height values from the array,
# and calculates the mean (average) and median (middle value) of the heights.

import numpy as np

# Sample data: each row is [height in inches, weight in pounds]
np_baseball = np.array([
    [180, 75.0],
    [190, 82.5],
    [170, 70.0],
    [185, 77.8],
    [175, 68.4]
])

# array[rows, columns]

# Create np_height_in from np_baseball
np_height_in = np_baseball[:, 0]  # Select all rows, first column (heights)

# Print out the mean of np_height_in
print("Mean height:", np.mean(np_height_in))  # Average of heights

# Print out the median of np_height_in
print("Median height:", np.median(np_height_in))  # Middle value when sorted

# Calculate and print average (mean) height
avg = np.mean(np_baseball[:, 0])
print("Average: " + str(avg))

# Calculate and print median height
med = np.median(np_baseball[:, 0])
print("Median: " + str(med))

# Calculate and print standard deviation of height
stddev = np.std(np_baseball[:, 0])
print("Standard Deviation: " + str(stddev))

# Calculate and print correlation between height and weight
corr = np.corrcoef(np_baseball[:,0], np_baseball[:,1])
print("Correlation: " + str(corr))


