#The try block of code will raise an error when trying to open non-existed python text file:

try:
    f=open("demofile.txt", "r")
    print(f.read())
except:
    print("Error reading file")
