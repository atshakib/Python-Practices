def gcd(a:int , b:int) -> int:
    while b!=0 :
        rem = a % b
        a = b
        b = rem
    return a

try: 
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(gcd(a,b))
except ValueError:
    print("Enter a valid input.")