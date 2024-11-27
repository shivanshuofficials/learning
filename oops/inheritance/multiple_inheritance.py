class employee:
    company = "microsoft"
    name = "shivanshu"
        
    def show(self):
        print(f"The name of employee is {self.name}. The company is {self.company}")


class coder:
    language = "python"
    
        
    def printlanguage(self):
        print(f"Out of all the languages, here is your language: {self.language}")


class programmer(employee,coder):
    company = "itc"
        
    def showlanguage(self):
        print(f"The name of employee is {self.name}. The language is {self.language}.")

# Create objects
a = employee()
b = programmer()

# Show company names
print(a.company, b.company)

b.show()
b.printlanguage()
b.showlanguage()
