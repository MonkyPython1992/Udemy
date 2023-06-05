#Create a Python program that calculates the profit for merchant price and customer price as a percentage

def ganancia(precio_venta,costo):
    return str((precio_venta - costo)/ precio_venta*100)+ "%"
    
print(ganancia(1000,300))