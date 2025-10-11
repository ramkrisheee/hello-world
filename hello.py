def main ():
    p= int(input("Enter a number: "))
    q= int(input("Enter another number: "))
    PRODUCT(p,q)
    
def PRODUCT(a,b):
    c = a * b
    print("The product of", a, "and", b, "is", c)   

main()