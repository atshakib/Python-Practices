def count_vowels(s: str) -> int:
    count = 0
    for char in s:
        if char.lower() == 'a' or char.lower() == 'e' or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u':
            count+=1
        else:
            continue
    return count

s = input("Enter your string: ")
print(count_vowels(s))