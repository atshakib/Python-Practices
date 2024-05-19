def rev(s: str) -> str:
    return s[::-1]

def is_palindrome(s: str) -> bool:
    result = []
    for char in s:
        if char.isalnum(): 
            result.append(char.lower())  

    cleaned_string = ''.join(result)
    return cleaned_string == rev(cleaned_string)

try:
    s = input("Enter your string: ")
    print(is_palindrome(s))
except ValueError:
    print("Please enter a valid string")
