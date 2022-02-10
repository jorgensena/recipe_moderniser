""" Get the recipe name from the user, check that input doesn't contain
numbers or is not left blank
Created by Amy Jorgensen
Version 2 : 10/06/21
"""


# Function to get recipe name and check it contains no numbers
def not_blank(question):
    error = "Your recipe name is blank or contains numbers!"
    valid = False
    while not valid:
        number = False  # Initial assumption that name doesn't contain digits
        response = input(question)

        for letter in response:  # Check for digits in recipe_name
            if letter.isdigit():
                number = True

        if not response or number == True:  # print error for blank name or digits
            print(error)

        else:
            valid = True
            return response


# Main routine
recipe_name = not_blank("What is the recipe name? ")
print("Today we are making {}, yum!".format(recipe_name))
