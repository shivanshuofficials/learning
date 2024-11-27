class anmimals:
    pass
class pet(anmimals):
    pass
class dog (pet):
    @staticmethod
    def bark():
        print("bow bow!")

d = dog()
d.bark()