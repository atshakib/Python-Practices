def if_prime(n: int) -> bool:
    if n <= 0:
        raise ValueError("Please enter a positive number.")
    for i in range(2,n):
        if n%i==0:
            return False
    return True

try: 
    n = int(input("Enter the number you want to check: "))
    print(if_prime(n))
except ValueError:
    print("Please enter a positive number.")