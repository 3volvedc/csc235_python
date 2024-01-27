# Carlton Austin Jr
# I placed everything in a function because why not, lol

# This function holds the ordering process.
def ordering_function():
    # User greeting
    print("Thank you for coming to the restaurant!\nPlease select from the items below:")
    # Base Options
    base_options = ["Bowl", "Burrito", "Tacos", "Salad"]
    # User input for the order base
    base = input(f"Please select a base\n{base_options}: ")
    # Protein Options
    protein_options = ["Chicken", "Steak", "Pork", "Veggies"]
    # User input for protein option
    protein = input(f"Please select a protein\n{protein_options}: ")
    # Greens Options
    greens_options = ["Iceberg Lettuce", "Green Lettuce", "Spinach", "Kale"]
    # User input for the greens
    greens = input(f"Please select a green\n{greens_options}: ")
    # Extra Options
    extras_options = ["Queso", "Guac", "Salsa", "Shredded Cheese"]
    # User input for the extras
    extras = input(f"Please select an extra\n{extras_options}: ")

    # creating a list of the ordered input items
    choices = [base, protein, greens, extras]
    # For loop that iterates over each element in the list 'choices'
    for item in choices:
        # Checks if the character length is 0, meaning nothing was input as a response,
        # then stop the program by way of raising a value error.
        if len(item) == 0:
            # ValueError to be raised if conditions are met
            raise ValueError(f"There is a choice missing!")
        # Checks if the character length is greater than 16 characters, more than the longest available option,
        # then stop the program by way of raising a value error.
        elif len(item) > 16:
            # ValueError to be raised if conditions are met
            raise ValueError(f"Missing order information, please check your selections again!")
        # Update the values in 'choices' using '.title()' to capitalize each word in the string
        choices = [item.title() for item in choices]
    # A string that with print a message as the conclusion of placing an order reading back the selections
    order_complete = f"Your {choices[0]} with {choices[1]}, {choices[2]}" \
                     f" and {choices[3]} has been ordered. Have a great day!"
    # return the string 'complete_order'
    return print(order_complete)


# run 'ordering_function()'
ordering_function()
