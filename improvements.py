## Adaptating if the person put a number (First example improvement)

letter = input("Letter: ").lower()
## here i tried to use only [] thinking it will carry all the numbers (it didnt work)

consonant = []
vowels = ["a", "e", "i", "o", "u"].lower()
number = [1, 100]  ## First, I tried to make num = [] thinking i could reach every number the person would type
                ## Then, I put only the number "10" and typed it in the terminal
                ## After that, this last version I made because of interval is possible to create between 1 to 99
                ## In the future, the best option is probably have a data downloaded which provides all the information needed 


if letter in vowels:  
    print("That´s a vowel!")
elif letter in consonant:
    print("Not a vowel!")
elif number:
    print("Well, that is a number, type a letter please!")
    

## Final version of the first example after studying other options (or not)



letter = input("Letter: ").lower().strip()
vowels = "aeiou"

if len(letter) != 1:
    print("Please type only one character!")
elif letter.isdigit(): ## .isdigit() is true from a number 0 to 9.
    print("Well, that is a number, please type a letter!")
elif not letter.isalpha():  ## isalpha() is true for letters, so this is not accepting things like: "!", "#".
    print("Please, type a letter!")
elif letter in vowels:  ## In this part the letter is tracked trhough vowels to see if that´s correct
    print("That´s a vowel!")
else: 
    print("That´s not a vowel! It´s a consonant")

## Final version of the first example after studying other options (i hope so)


vowels = "aeiou"


while True:
    letter = input("Letter: ").lower().strip()
    if letter.isdigit():
        print("Well, that is a number, type a letter please!")
    elif len(letter) != 1:
        print("Please type only one character.")
    elif not letter.isalpha():
        print("That's not a letter, try again!")
    elif letter in vowels:
        print("That's a vowel!")
        break
    else:
        print("Not a vowel! It's a consonant.")
        break

                    # It worked!!!
