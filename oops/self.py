class Employee: #This is a class attribute
  
    language ='py'
    salary=20000

    def getinfo(self):
        print(f"the language is {self.language}.\nthe salary is{self.salary}")
    def greet(self):
        print(f"Goood Morning!")

shivanshu = Employee()
shivanshu.greet()
shivanshu.getinfo()