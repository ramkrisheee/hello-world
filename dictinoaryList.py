car = {
    "Toyota": "Corolla",
    "Honda": "Civic",   
    "Ford": "Mustang"
}
car.update({"BMW": "X5"})
print (car.get("Honda","unknown"))

def availability(dicn):
    print("Available car models:")
    for key in dicn:
        print(f"With manufacture {key} and their model {dicn[key]} You have a discount",end="\n")

    for key,value in dicn.items():
        print(f"key value {key} and their model {value} You have a total discount",end="\n")   
    
    for key in dicn.keys():
        print(f"Key {key} and their model {dicn[key]} You have a total discount",end="\n")   
    
    for value in dicn.values():
        print(f"With manufacture and their model {value} You have a total discount",end="\n")   


def main():
    availability(car)
main()
