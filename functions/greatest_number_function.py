def greatest(a,b,c):
    if(a>b and a>c):
        print("A=")
        return a
    elif(b>a and b>c):
        print("B=")
        return b
    elif(c>a and c>b):
        print("C=")
        return c
    
a = int(input("enter A:"))
b = int(input("enter b:"))
c = int(input("enter c:"))

print(greatest(a,b,c))