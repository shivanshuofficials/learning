a = int(input("enter the number a:"))
b = int(input("enter the number b:"))

if (b ==0):
    raise ZeroDivisionError("the nmber cannot be divided by zero")
else:
    print(f"the division of a/b is:{a/b}")