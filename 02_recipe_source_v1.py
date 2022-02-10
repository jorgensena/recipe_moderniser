""" Get the recipe source from the user, checking that input is not left blank
 and allowing user to allow or disallow digits.
Created by Amy Jorgensen
Version 1 : 14/06/21
"""


# Function to get recipe name and check it contains no numbers
def not_blank(question, error_msg, allow_num):
    error = error_msg
    valid = False
    while not valid:
        number = False  # Initial assumption that name doesn't contain digits
        response = input(question)

        if not allow_num:
            for letter in response:  # Check for digits in recipe_name
                if letter.isdigit():
                    number = True

        if not response or number == True:  # print error for blank name or digits
            print(error)

        else:
            return response


# Main routine
source = not_blank("Where is the recipe from? ",
                   "The recipe source can't be blank",
                   True)
print("\nThis recipe is from {}".format(source))
