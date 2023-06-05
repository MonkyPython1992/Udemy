#Create a class named User and create a way to check the number of users (number of instances) were created, 
# so that the value can be accessed as a class attribute.

class User:
    contador=0
    
    def __init__(self):
        User.contador+=1
        
    
    def num_users():
        return "Number of instances created: " + str(User.contador)


p1=User()
p2=User()
print(User.num_users())
        