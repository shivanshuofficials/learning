#sum of natural numbers from 0 to 10
def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n 
n = int(input("ente teh number:"))
print(sum(n))