class Employee: #This is a class attribute
  
    language ='py'
    salary=20000
     
    def __init__(self,language,salary) :#dunder methhod automatically called
        self.language =language
        self.salary =salary
        
        print("I am creating an object")

    
    def getinfo(self):
        print(f"the language is {self.language}.\nthe salary is{self.salary}")
    
    
    @staticmethod
    def greet():
        print(f"Goood Morning!")

shivanshu = Employee("python",100000)

print(shivanshu.language,shivanshu.salary)