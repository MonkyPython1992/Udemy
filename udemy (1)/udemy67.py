#Create a Python program that determines whether a shopping order is eligible for free shipping. 
# An order is eligible for free shipping if the total cost of items purchased exceeds $100

compra={"queso":45,"pan":30,"arroz":30}
def free_shipping(order):
    if sum(order.values())>100:
        return "Eligible for free shipping"



print(free_shipping(compra))