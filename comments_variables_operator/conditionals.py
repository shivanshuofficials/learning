# Input: Get the user's age
age = int(input("Please enter your age: "))

# Using if-elif-else to categorize the age
if age < 13:
    print("You are a Child.")
elif 13 <= age < 18:
    print("You are a Teenager.")
elif 18 <= age < 65:
    print("You are an Adult.")
else:
    print("You are a Senior.")
