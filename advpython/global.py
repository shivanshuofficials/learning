a = 89
def fun():
    global  a # it modified the variable outside the function
    a = 3
    print(a)

fun()
print(a)
