## Examples of if, elif and else (First example)

letter = input("Letter: ").lower()

if letter in "aeiou":
    print("Vowel")
else:
    print("Not a vowel!")

## Basic example (Second example)

age = int(input("Put your age: "))

if age >= 18:
    print("You have permission!")
elif age >= 13:
    print("You are underage!")
else:
    print("What are you doing, you are a child!!!")

