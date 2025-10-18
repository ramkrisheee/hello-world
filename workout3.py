""" while True:
    try:
        fuel_status = input("Enter fuel level in fraction Eg.1/2, 3/4 etc. : ")
        num, denom = fuel_status.split("/")
        num = float(num)
        denom = float(denom)
        if denom == 0 or num > denom:   
            raise ValueError
        y= round(((num/denom)*100))
        if y <= 1:
            print("E")
        elif y >= 99:
            print("F")
        else:
            print(f"{y} %")
            break
    except ValueError:
        print("Invalid input")
        continue """

""" menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
    "Bowl": 4.50,
    "Bowl": 1
}

item = str(input("Enter the item name:")).title()
total=0

while item != "":
    if item in menu.keys():
        total += menu[item]
        print (f"Total: ${total}")
        item = str(input("Enter the item name:")).title()
    else:
        item = str(input("Enter the item name:")).title() """
    
""" import sys
lines = sys.stdin.read().splitlines()
print(lines)

trim_list = [tline.strip().upper() for tline in lines]
trim_list.sort()
print(trim_list)


list = [str(trim_list.count(line)) + " " + line  for line in trim_list]
dedupes=[]
for dedupe in list:
    if dedupe not in dedupes:
        dedupes.append(dedupe)
print("\n".join(dedupes))

#final_list= list. """

def main():

   

#def get_input(in_date):
    in_date=input("Enter date in format:")
    in_date= in_date.replace("/"," ").replace(","," ").split(" ")
   #print (in_date)
    while True:
        try:
            if valid_year(in_date[2]) is not None and valid_month(in_date[0].title()) is not None and valid_date(in_date[0].title(),in_date[1]) is not None:
                print(f"Standard format {valid_year(in_date[2])}-{valid_month(in_date[0].title())}-{valid_date(in_date[0].title(),in_date[1])}")
                break
            else:
                in_date=input("Enter date in format:")
                in_date= in_date.replace("/"," ").replace(","," ").split(" ")
        except IndexError:
            in_date=input("Enter date in format:")
            in_date= in_date.replace("/"," ").replace(","," ").split(" ")


def valid_month(month):
    global months
    if month=="January" or month=="1" or month=="01":
        return "01"
    elif month=="February" or month=="2" or month=="02":
        return "02"
    elif month=="September" or month=="9" or month=="09":
        return "09"

def valid_year(year):
    if year.isnumeric()==True and len(year)==4:
        return year

def valid_date(m1,dt):
    try:
        if dt.isnumeric()==True and ((valid_month(m1) in ["01","03","05","07","08","10","12"] and int(dt)>0 and int(dt)<32) or (valid_month(m1) in ["04","06","09","11"] and int(dt)>0 and int(dt)<31) or (valid_month(m1) in ["02"] and int(dt)>0 and int(dt)<29)):
            return dt.rjust(2,"0")
    except ValueError:
       """  break
    except NameError:
        break """



main()

