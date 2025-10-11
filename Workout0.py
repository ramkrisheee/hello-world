
def conver(a):
    C=3.24*10**6
    b=a*C**2
    return b

def main():
    ab=input("Enter the mass: ")
    if  ab.isnumeric()==False:
        print("Invalid input")
    else:
        ab=int(ab)
        print(str(conver(ab)) + " J")

main()




