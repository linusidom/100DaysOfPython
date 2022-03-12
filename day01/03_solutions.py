
"""

Print statement Solutions

"""

# Pause the video and try to solve these one by one on your own

print("Day 1 - This is a string")
print("String Concatentation is done with the + sign")
print('up oh...Am I in too deep?')
print(("Is the parentheses closed or open...?"))
print("Is everything spelled correctly?")
print(f'What is this f at the beginning for?')
print("What's the deal with all these quotes?")


"""

Variable Manipulation

"""

a = input('A: ')
b = input('B: ')

#################
#Solution Goes here - Do not change the code above or below
# Order of lines matters
# Python is what is known as synchronous
# Commands run in the order they appear


temporary_variable = a
a = b
b = temporary_variable



#################

print(f'A should equal B: {a}')
print(f'B should equal A: {b}')





"""
User Input - Challenge 1

Ask for the users First and Last name
Print the following "Hello First Name Last Name, how are you?"

Hint try this with string concatenation

"""
# Your solution goes here
first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
print("Hello" , first_name , last_name, "how are you?")


"""
User Input - Challenge 2

Create a pet name generator
Ask for the the users favorite flavor of ice cream
and favorite day of the week

Output the 2 answers combined as a suggestion for the pets name

Hint try to solve this with string formatting

"""

# Your solution goes here
# Python uses snake_case for variable and function names
# Python uses Pascal Case for Classes (in the future)

# JavaScript uses camelCase for variables and functions
# JavaScript uses TitleCase for Classes

ice_cream = input('What is your favorite flavor of Ice Cream? ')
day_of_the_week = input('What is your favorite day of the week? ')
print(f'You should name your pet {ice_cream} {day_of_the_week} :)')