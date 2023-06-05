#Given a class for a BasicPlan, write the classes for StandardPlan and PremiumPlan which have class attributes

class BasicPlan:
    can_stream=True
    can_download=True
    has_SD = True
    has_HD = False
    has_UHD = False
    num_of_devices=1
    price="$8.99"

class StandardPlan(BasicPlan):  #Hereda
    num_of_devices = 2
    has_HD = True
    price = "$12.99"

class PremiumPlan(StandardPlan): #hereda
    num_of_devices = 4
    has_UHD = True
    price = "$15.99"