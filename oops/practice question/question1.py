class Programmer:
    company = "Microsoft"
    def  __init__(self,name,salary,pincode):
        self.name = name
        self.salary = salary
        self.pincode = pincode

p = Programmer("shivanshu",1000000,201010)
print(p.name,"\n",p.salary,"\n",p.pincode,"\n",p.company,"\n")
r = Programmer("rohan",1000000,201010)
print(r.name,"\n",r.salary,"\n",r.pincode,"\n",r.company,"\n")
