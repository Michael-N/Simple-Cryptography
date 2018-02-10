maxKeySize = 26

#set program to encrypt or decrypt based on user input
mode = input("Encrypt or Decrypt? (enter 'e' or 'd')\n").lower()

if mode != "e" and mode != "d":
    print("Invalid selection.")
    quit()
message = list(input("Enter message.\n"))
shift = int(input("Enter shift value.(integer 1-26)\n"))
if shift > maxKeySize or shift < 1:
    print("Invalid selection.")
if mode  == "d":
    shift = -shift

def translator():
    translated = ""
    for symbol in message:
        if symbol.isalpha():
            num = ord (symbol)
            num += shift

            if symbol.isupper():
                if num > ord("Z"):
                    num -= 26
                elif num < ord("A"):
                    num += 26
            if symbol.islower():
                if num > ord("z"):
                    num -= 26
                elif num < ord("a"):
                    num += 26
            character = chr(num)
            translated += (character + " ")
        else:
            translated += (symbol + " ")
    return translated
print(translator())
