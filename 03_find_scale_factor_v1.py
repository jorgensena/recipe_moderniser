""" Ask user for number of servings in recipe and number of servings desired
and then calculate the scale factor
Created by Amy Jorgensen
Version 1 : 16/06/21
"""

# Get serving size
serving_size = float(input("What is the recipe serving size? "))

# Get desired number of servings
desired_size = float(input("How many servings would you like: "))

# Calculate scale factor
scale_factor = desired_size / serving_size

# Print scale factor
print("Scale Factor: {}".format(scale_factor))
