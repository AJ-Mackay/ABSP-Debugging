# Module 12 - Debugging: Using the Debugger

print('Enter the first number to add:')
first = input()
print('Enter the second number to add:')
second = input()
print('Enter the third number to add:')
third = input()
# print('The sum is ' + first + second + third) # String concatenation, not maths.
# print('The sum is ' + str(int(first) + int(second) + int(third)) + '.') # My Fix.
numbers = int(first) + int(second) + int(third)
print(f'The sum is {numbers}.') # Andrew's suggestion.

# The sum was not added as the inputs were saved as strings by default.

### I FIXED IT MYSELF! ###
### I didn't know if "str(int())" would work ###
### so I tried it on a whim, and it did! ###

### I then switched it to using "f' {numbers}" at Andrew's suggestion ###
### This removed the need for using str(), which is much neater. ###
