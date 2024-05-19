def find_largest(numbers: list) -> int:
    largest = 0
    for number in numbers:
        if number > largest:
            largest = number
    return largest

try:
    numbers = []
    n = int(input("How many element will there be in your list? "))
    print(f"Enter {n} numbers by pressing 'enter' after every input: ")
    for i in range(0,n):
        ele = int(input())
        numbers.append(ele)
    print(find_largest(numbers))
except ValueError:
    print("Enter only integers as input.")