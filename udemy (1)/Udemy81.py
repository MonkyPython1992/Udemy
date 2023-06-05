#Create a Python program that takes in the number of each challenge level a user has played 
# and calculates the user's total number of points.
# 5 points easy, 10 points medium, 20 points hard.

def score(easy,med,hard):
    puntos=(easy*5) + (med*10)+(hard*20)
    return puntos

print("Total points: ",score(5,3,1))
    