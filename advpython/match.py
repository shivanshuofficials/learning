def describe_number(value: int):
    match value:
        case 0:
            print("Zero")
        case 1:
            print("One")
        case 2:
            print("Two")
        case _:
            print("Another number")

# Testing the function
describe_number(0)  # Output: zero
describe_number(1)  # Output: One
describe_number(2)  # Output: two
describe_number(5)  # Output: Another number
