#Create a method in the Person class which returns how another person's age compares. 
#Given the objects p1, p2 and p3, which will be initialized with the attributes name and age, 
#return a sentence in the following format: {other_person} is {older than / younger than / the same age as} me

class Person:
    def __init__(self,age,name):
        self.name=name
        self.age=age
        self.my_age=30
        
    def age_compares(self):
        if self.age > self.my_age:
            return self.name + " is older than me"
        elif self.age < self.my_age:
            return self.name + "  is younger than me"
        else:
            return self.name +" is the same age as me"
            

p1=Person(35,"Manuel")
print(p1.age_compares())
p2=Person(20,"Nicolas")
print(p2.age_compares())
p3=Person(30,"Ivan")
print(p3.age_compares())

        