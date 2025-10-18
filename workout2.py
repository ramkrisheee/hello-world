""" def camel_to_snake(a):
#a = "CamelCase"
    b=list(a)
    c=''

    for l in range(len(b)):
        if b[l] ==' ':
            c=c
        elif l >1 and b[l].isupper():
            b[l]='_'+ b[l].lower()
            c = c + b[l]
        else:
            b[l]=b[l].lower()
            c = c + b[l]
    return c
        
        #print(b[l],end='')

def main():
    CamelCase=str(input('Enter a input: '))
    print("output: " + camel_to_snake(CamelCase))
  
   
main()
 """

""" 
def remove_vowels(s):
    vowels = 'aeiouAEIOU'
    result = ''.join([char for char in s if char not in vowels])
    return result

def main():
    input_string = input("Enter a string: ")
    output_string = remove_vowels(input_string)
    print("String after removing vowels:", output_string)

main() """

""" def main():
    plates = []
    print(plates)
    plate = str(input("Enter Plate number or type E to exit: "))    
    while plate != 'E':   
        c=  is_valid(plate)  
        if c is True and plate not in plates:
            plates.append(plate)
            print("Valid plate number added")
            #break
        elif c is True and plate in plates:
            print( plate + " number already used ")
        else:
            print (plate + "is an invalid plate") 
        print(plates)
        plate = input("Enter Plate number or type E to exit: ")
        
        
            
def is_valid(s):
    c=0
    if len(s) >= 2 and len(s) <= 6  and s[:2].isalpha() == True and s.isalnum()==True : 
        c=1
        for i in range(len(s)):
            if s[i].isdigit():
                a1=i
        for j in range(len(s)):
            if s[j].isalpha():
                a2=j
        if a2 > a1:
            c=0
        s1 =''.join([char for char in s if char.isdigit()==True ]) #and s[char+1].isdigit()==True
        if s1[:1]=='0':
            c=0
    
    if c==1:
        return True
    else:
        return None
        
main() """

""" fruits =[{"fruit":"Apple","Calorie":"130","portion":"1 large 250g"},
         {"fruit":"Avocado","Calorie":"50","portion":"1/3 medium 50g"},
         {"fruit":"Banana","Calorie":"110","portion":"1 small 101g"},
         {"fruit":"Cantaloupe","Calorie":"50","portion":"1 cup 177g"},
         {"fruit":"Grapefruit","Calorie":"60","portion":"1/2 medium 123g"},
         {"fruit":"Grapes","Calorie":"90","portion":"1 cup 151g"},
         {"fruit":"Honeydew Melon","Calorie":"50","portion":"1 cup 177g"},
         {"fruit":"Kiwifruit","Calorie":"90","portion":"2 medium 148g"},
         {"fruit":"Lemon","Calorie":"15","portion":"1 medium 58g"},
         {"fruit":"Lime","Calorie":"20","portion":"1 medium 67g"},
         {"fruit":"Mango","Calorie":"135","portion":"1/2 medium 100g"},
         {"fruit":"Nectarine","Calorie":"60","portion":"1 medium 130g"},
         {"fruit":"Orange","Calorie":"80","portion":"1 medium 131g"},
         {"fruit":"Peach","Calorie":"60","portion":"1 medium 130g"},
         {"fruit":"Pear","Calorie":"100","portion":"1 medium 178g"},
         {"fruit":"Pineapple","Calorie":"80","portion":"1 cup 165g"},
         {"fruit":"Plums","Calorie":"30","portion":"1 small 66g"},
         {"fruit":"Raspberries","Calorie":"65","portion":"1 cup 123g"},
         {"fruit":"Strawberries","Calorie":"50","portion":"1 cup 152g"},
         {"fruit":"Tangerine","Calorie":"50","portion":"1 medium 109g"},
         {"fruit":"Watermelon","Calorie":"80","portion":"2 cups diced 280g"}]

def main():
    total_calories=0
    fruit_name = input("Enter the fruit name: ").strip().title()
    for fruit in fruits:
        if fruit["fruit"] == fruit_name:
            print(f"{fruit['portion']} of {fruit['fruit']} contains {fruit['Calorie']} calories.")
            total_calories += int(fruit['Calorie'])
            break
    else:
        print("Fruit not found in the database.")

main() """
    
fruits = [{"Apple":"130","Mango":"80","Strawberry":"150","Banana":"110","Grapes":"90"}]
def main():
    fruit_name= input("Enter the fruit name: ").strip().title()
    for fruit in fruits:
        print(fruit)
        if fruit_name in fruit:
            print(f"{fruit_name} contains {fruit[fruit_name]} calories.")
            break
        else:
            print("Fruit not found in the database.")
main()