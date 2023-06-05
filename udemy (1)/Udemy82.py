#Create a Python program that returns the number of decimal places a number has. Any zeros after the decimal point 
# count towards the number of decimal places.

def decimal(n):
    num_decimales = len(str(n)[str(n).find("."):])-1
    return num_decimales

print("Num of decimals:",decimal(3.1524))