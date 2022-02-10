""" Ask user for number of servings in recipe and number of servings desired
and then calculate the scale factor
Version 2: Get's the scale factor and warns user if it is too large or small
Created by Amy Jorgensen
Version 1 : 21/06/21
"""


# number checking function
# Gets the scale factor - which must be a number
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


# Main routine
keep_scale = False
while not keep_scale:

    # Get serving size and check it's a number
    serving_size = num_check("What is the recipe serving size? ")
    # Get desired number of servings and check it's a number
    desired_size = num_check("How many servings would you like: ")
    # Calculate scale factor
    scale_factor = desired_size / serving_size

    # Warn the user if the scale factor is less than 0.25 or more than 4
    if scale_factor < 0.25:
        print("Scale Factor: {}".format(scale_factor))
        print("Warning! This scale factor is very small and you might "
              "\nstruggle to accurately weigh the ingredients."
              "\nPlease consider having more servings and freezing the "
              "left overs.")
        change_scale = input("Press <enter> to keep this scale, "
                             "or <any key> and <enter> to change it: ")
        if not change_scale:
            keep_scale = True

    elif scale_factor > 4:
        print("Scale Factor: {}".format(scale_factor))
        print("Warning! This scale factor is quite large and you might "
              "\nstruggle to fit everything in the bowl. "
              "\nPlease consider having less servings and making more "
              "than one batch.")
        change_scale = input("Press <enter> to keep this scale, "
                             "or <any key> and <enter> to change it: ")
        if not change_scale:
            keep_scale = True

    else:
        keep_scale = True


# Print scale factor
print("Scale Factor: {}".format(scale_factor))
