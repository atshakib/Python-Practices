def fibonacci(n: int) -> int:
    if n<0:
        raise ValueError("Input cannot be a negative number!")
    elif n==0:
        return 0
    elif n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

try:
    n = int(input("Enter the number: "))
    print(fibonacci(n))
except ValueError:
    print("Please enter a valid input")
    