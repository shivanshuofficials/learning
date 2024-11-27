class employye:
    company = "microsoft"
    def show(self):
        print(f"The name of employee is {self.name}.the salary is{self.salary} ")

class programmer(employye):
     company = "itc"
     def showlanguage(self):
           print(f"The name of employee is {self.name}.the salary is{self.salary} ")


a = employye()
b = programmer()

print(a.company,b.company)