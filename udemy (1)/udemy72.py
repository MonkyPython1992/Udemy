#Write a Python program that check if a number is even or odd number?

def even_odd(n):
    if n%2==0:
        return "The number is even"
    else:
        return "The number is odd"

print(even_odd(255778))
print(even_odd(988779))