def main():
    time = input("Enter time in 24 hour format Eg: HH:MM: ")
    converted_time = convert(time)
    #print(converted_time)
    if 7.00 <= converted_time <= 8.00:
        print("Breakfast time")
    elif 12.00 <= converted_time <= 13.00:
        print("Lunch time") 
    elif 18.00 <= converted_time <= 19.00: 
        print("Dinner time")
    else:
        print("No meal time")   

def convert(user_time):
    hour, minute = str(user_time).split(":")
    hour = int(hour)
    minute = (int(minute)/60)*100
    return float(f"{hour}.{minute:.0f}")

main()

