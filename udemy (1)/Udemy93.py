#Create a Python program that handle the error of accessing an item by a non existent index

x = [2, 5, 10, 25, 17, 30, 44]
while True:
    i = input("Coloque el numero de index que desea buscar, o escriba s para salir.Index: ")
    if i == 's':
        break
    try:
        i = int(i)
        print(x[i])
    except ValueError:
        print('Has to be a integer')
    except IndexError:
        print('no item in that index = ', i)
