# Initialize a variable
i = 0

# Loop while i is less than 5
while i < 5:
    print(i)
    i += 1  # Increment i to avoid infinite loop

# Infinite loop
while True:
    user_input = input("Type 'exit' to quit: ")
    if user_input == "exit":
        print("Exiting loop.")
        break
    else:
        print("You typed:", user_input)
