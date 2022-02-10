""" Ask user for number of servings in recipe and number of servings desired
and then calculate the scale factor
Version 2: uses number checking function to ensure input is a number
Created by Amy Jorgensen
Version 1 : 16/06/21
"""

# number checking function
def num_check(question):
    valid = False
    error = "Please enter a number, higher than 0"
    while not valid:
        try:
            response = float(input(question))
            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)

# Get the scale factor - which must be a number
# Get serving size
serving_size = num_check("What is the recipe serving size? ")

# Get desired number of servings
desired_size = num_check("How many servings would you like: ")

# Calculate scale factor
scale_factor = desired_size / serving_size

# Print scale factor
print("Scale Factor: {}".format(scale_factor))
