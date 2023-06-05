#Use Subclass(Parentclass) to define a child classes of gender.


class Person():
    def get_gender(self):
        return "Genero"
    
class Male(Person):
    def get_gender(self):
        return "Male"

class Female(Person):
    def get_gender(self):
        return "Female"
        
male=Male()
female=Female()

print(male.get_gender())
print(female.get_gender())