#Write Python program to Convert hours into seconds?.How many seconds in 5 hours?

def hour_to_second(hour):
    minutes= hour*60
    seconds= minutes*60
    return "Total of seconds: "+ str(seconds)

print(hour_to_second(5))
    