class number:
    def __init__(self,n) :
        self.n = n

    def __add__(self,num):
        return self.n + num.n
'''
__add__
__sub__
__mul__
__truediv__
__floordiv__
'''
    
n = number(1)
m = number(2)

print(n + m)
        