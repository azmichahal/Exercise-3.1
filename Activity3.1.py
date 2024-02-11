# Exercise 1
# Empty list to store the output numbers 
n = [] 

# Create a for loop to test the values 
for i in range(1500, 2701):
    
    # Create an if statement to apply the conditions
    if (i % 7 == 0) & (i % 5 == 0):
        n.append(i)

# Print the result 
print (n) 

#---------------------------------------------------------------------------------------#

# Exercise 2
# Take values from users
temp = input("Input the temperature you want to convert eg. 30C or 95F")

# Extract the numerical value from input
degree = int(temp[:-1])

# Identify the unit
d_unit = temp[-1]

# Conversion from Fahrenheit to Celsius
if d_unit.upper() == "F": 
    result = int(5 * (degree - 32) / 9)
    unit = "Celsius"

# Conversion from Celsius to Fahrenheit
elif d_unit.upper() == "C":
    result = int(((9 * degree) + (32 * 5)) / 5)
    unit = "Fahrenheit"

# Create a condition to break incase input is invalid
else: 
    quit()

print ("The temperature in", unit, "is", result, "degrees")

#---------------------------------------------------------------------------------------#

# Exercise 3
import random

target_num, guess_num = random.randint(1,10), 0

while guess_num != target_num:
    guess_num = int(input("Guess the number"))

print("Correct")

#---------------------------------------------------------------------------------------#

# Exercise 4

n = 5

for i in range (n):
    for j in range(i):
        print ('* ', end="")
    
    print ('')

for i in range (n, 0, -1):
    for j in range(i):
        print ('* ', end="")
    
    print ('')
    
#---------------------------------------------------------------------------------------#
   
# Exercise 5

# Take word from user
Test_str = str(input("Write a word to be reversed: "))

# Reverse the word and print it
print(Test_str[::-1])



