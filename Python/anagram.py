def are_anagrams(s1: str , s2: str) -> bool:
    s1_cleaned = ''.join(char.lower() for char in s1 if char.isalnum())
    s2_cleaned = ''.join(char.lower() for char in s2 if char.isalnum())

    if(len(s1_cleaned) != len(s2_cleaned)):
        return False
    else:
        return sorted(s1_cleaned) == sorted(s2_cleaned)

try:
    s1 = input("Enter first word: ")
    s2 = input("Enter second word: ")
    print(are_anagrams(s1,s2))
except:
    print("Enter valid input.")

           
