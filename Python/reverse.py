def reverse_string(s: str) -> str:
    if s <= 1:
        return s
    return s[::-1]

s = input("Enter the string: ")
print(reverse_string(s))