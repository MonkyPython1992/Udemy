#Create a class representing a concert ticket.Its constructor takes two values: a ticket price,and a section.
#Sections = {'lower', 'premier', 'mezzanine', 'floor'}

class Ticket():
    def __init__(self,price,section):
        self.price=price
        self.section=section
    
    def show_ticket(self):
        return "You have a Ticket for section: " + self.section + ". The Price is: "+str(self.price)


tkt1=Ticket(199,"premier")
tkt2=Ticket(400,"mezzanine")

print(tkt1.show_ticket())
print(tkt2.show_ticket())