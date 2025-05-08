# Exercise 0: Example
#
# This is a practice exercise to familiarize you with basic Python data structures.
#
# Create a list called `example_list` and append three elements to it. Print each element using a loop.
#
# Requirements:
# - The list should contain any three elements of your choice.
# - Use a loop to print each element.

def example_list_function():
  example_list = ['element1', 'element2', 'element3']
  for element in example_list:
      print(element)

# Call the function and print each element
example_list_function() # output: element1, element2, element3

# ----------------------------------------------------------------------------------------------------------------

# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    students = ['Bob', 'David', 'John'] # List of student names
    first_student = students[1] #Lists are 0-indexed in Python. 
    last_student = students[-1] #Negative indexing is allowed. -1 refers to the last element in the list.
    return (first_student, last_student) # Returning a tuple with both values so we can print them together

# Call the function and print the result
print('Exercise 1:', manage_students()) # output: ('David', 'John')

# ----------------------------------------------------------------------------------------------------------------

# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.

def combine_foods():
    foods = ('hotdog', 'sandwhich', 'fried chicken') # Tuple of food items
    meal = '' # Initialize an empty string
    for food in foods: # Loop through each food item in the tuple
        meal += food + ' ' # Add the food item and a space to the end of the current string

    return meal.strip() # .strip() removes any trailing space at the end of the string

# Call the function and print the result
print('Exercise 2:', combine_foods()) # output: 'hotdog sandwhich fried chicken'

# ----------------------------------------------------------------------------------------------------------------

# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.

def slice_foods():
    foods = ('hotdog', 'sandwhich', 'fried chicken') # Define the tuple of the same foods

    last_two_foods = foods [-2:] # Slicing the tuple to get the last two items

    return last_two_foods # Return the sliced tuple

# Call the function and print the result
print('Exercise 3:', slice_foods()) # output: ('sandwhich', 'fried chicken')

# ----------------------------------------------------------------------------------------------------------------

# Exercise 4: Dictionaries and String Formatting
#
# Create a dictionary named home_town containing the keys of city, state, and population.
# Using the home_town dictionary, assign to a variable named home_town_message a string with this format: “I was born in <city>, <state> - population of <population>”

def hometown_info():
    home_town = { # Dictionary with key-value pairs, denoted with {}
        'city': 'Coral Springs',
        'state': 'Florida',
        'population': 134000
    }

    # Using string formatting to create the message
    home_town_message = f'I was born in {home_town["city"]}, {home_town["state"]} - population of {home_town["population"]}.' # dict['key'] returns the value
    
    return home_town_message # Return the formatted string

# Call the function and print the result
print('Exercise 4:', hometown_info()) # output: I was born in Coral Springs, Florida - population of 134000.

# ----------------------------------------------------------------------------------------------------------------

# Exercise 5: Iterating Over Dictionary Items
#
# Define an empty list named home_town_items.
# Use a for loop to iterate over the key: value pairs in the home_town dictionary and append a string with the following format to home_town_items: "<key> = <value>"

def list_home_town_items():
    home_town = { # Dictionary with key-value pairs, denoted with {}
        'city': 'Coral Springs',
        'state': 'Florida',
        'population': 134000
    }

    home_town_items = [] # Initialize an empty list

    for key, value in home_town.items(): # Loop through each key-value pair in the dictionary and .items() returns key-value pairs
        home_town_items.append(f'{key} = {value}') # Append the formatted string to the list

    return home_town_items
    

# Call the function and print the result
print('Exercise 5:', list_home_town_items()) # output: ['city = Coral Springs', 'state = Florida', 'population = 134000']

# ----------------------------------------------------------------------------------------------------------------
