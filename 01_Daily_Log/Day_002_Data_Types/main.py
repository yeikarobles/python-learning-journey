# TASK 1 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Strings
    # Subscripting

print("Hello"[0])

# 2. Integer

print(123+456)

# Large integer

print(123_456_789)

# 3. Float = Floating Point Numbers

print(3.1415)

# 4. Boolean

print(True)

print(False)

# Quiz

street_name = "Abbey Road"
print(street_name[4] + street_name[7])

# TASK 2 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Type Errors, checking and conversion 

print(type(False))
print(type(3.1415))
print(type(123_456_789))
print(type(123+456))
print(type("Hello"[0]))

# Convnersion

int()
float()
str()
bool()

# Fix the error 

# 1
print(
    f"Number of letters in your name: {len(input("Enter your name\n"))}"
)

# 2
print(
    "Number of letters in your name: " +  str(len(input("Enter your name\n")))
)

# 3
user_name = input("Enter your name\n")
name_length = len(user_name)

print(
    "Number of letters in your name", name_length
)

# TASK 3 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Mathematical oparations

# PEMDAS LR 
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction (left to rigth)
# 

print(123 + 456)
print(7 - 3)
print(3 * 2)
print(6 / 3) # return float
print(6 // 3) # return int
print(2 ** 3) 

print(3 * 3 + 3 / 3 - 3) # result = 7

print(3 * (3 + 3) / 3 - 3) # result = 3

# TASK 4 --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Number manipulation

# BMI Calculator
# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:

# bmi is equal to the person's weight divided by the person's height squared.

# Convert this sentence into code on line 6.

height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / (height**2)

print(bmi)

# floor the number 
print(int(bmi)) # outcome 30

print(round(bmi)) # outcome 31

print(round(bmi, 2)) # you can tell the function how many decimals (.xx) you would like to have

# Assignment operators
#   assignment operators will add the number on the right to the original value of the variable on the left and assign the new value to the variable.

# +=
# -=
# *=
# /=

score = 0

score +=1
print(score) # new value assigned 

 # f-strings 
print(f"Your score is = {score}")

a = int("5") / int(2.7) # converting a str and a float into an int
print(a) # outcomne 2.5 type float 
# int always round the number down 
# 5/2 = 2.5
# float because the use of / and not // 


# Which of these lines of code will give you an error?
name = input("What is your name? ")
print(f"Hello, {name}")

print("Hello, " + name)

age = 12
print(f"You are {age} years old")

print("You are " + age + " years old") # TypeError: can only concatenate str (not "int") to str

