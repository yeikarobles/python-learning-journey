print("hello world! This is the Band Name Generator.") 

#task 1
#Printing Practice

print(
    "1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.\n" 
    "2. Knead the dough for 10 minutes.\n"
    "3. Add 3g of Salt.\n"
    "4. Leave to rise for 2 hours.\n"
    "5. Bake at 200 degrees C for 30 minutes.")

print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")

#task  2
#Fix the code below 👇

print("Notes from Day 1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the + sign")
print("New lines can be created with a \ and the letter n")


#task 3
#Update the code to add excamation mark
print("Hello " + input("What is your name?") + "!")

# task 4
# Check the length of the string

name = input("What is your name?")
name_lenght = len(name)
print (name)
print (name, "has", name_lenght, "letters")

#one line 
print(len(input("What is your name?")))

#task 5 
#Write 3 lines of code to switch the contents of the variables

glass1 = "milk"
glass2 = "juice"

# #Swap values
glass1, glass2 = glass2, glass1

print("glass1 is now:", glass1)
print("glass1 is now:", glass2)


time_until_midnight = "5"
print("there are "+time_until_midnight+" hours until midnight")