#Write a function to compute 5/0 and use try/except to catch the exceptions.

def exception():
    try:
        5/0
    except:
        return "cannot be divided by zero"
print(exception())