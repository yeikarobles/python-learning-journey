# Header
print("Welcome to the tip calculator!")

# variables to store data
bill = input("What was the total bill?\n $")
tip = input("How much tip would you like to give? 10, 12, or 15?\n")
people_quantity = input("How many people to split the bill?\n")

# calculations

percentage = (int(tip)/100)+1 # calculate the percentage 

total = float(bill)*percentage # sum the percentage to the bill to obtain a total

split_total = total / int(people_quantity) # divide the total between the amount of people 

# outcome
print(f"Each person should pay: ${split_total:.2f}") 
