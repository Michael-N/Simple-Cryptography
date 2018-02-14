import math
from datetime import datetime
# creating rotors
rotor_I = [ord("d"),ord("m"),ord("t"),ord("w"),ord("s"),ord("i"),ord("l"),ord("r"),ord("u"),ord("y"),\
    ord("q"),ord("n"),ord("k"),ord("f"),ord("e"),ord("j"),ord("c"),ord("a"),ord("z"),ord("b"),ord("p"), \
    ord("g"),ord("x"),ord("o"),ord("h"),ord("v")]
rotor_II = [ord("h"),ord("q"),ord("z"),ord("g"),ord("p"),ord("j"),ord("t"),ord("m"),ord("o"),ord("b"),\
    ord("l"),ord("n"),ord("c"),ord("i"),ord("f"),ord("d"),ord("y"),ord("a"),ord("w"),ord("v"),ord("e"), \
    ord("u"),ord("s"),ord("r"),ord("k"),ord("x")]
rotor_III = [ord("u"),ord("q"),ord("n"),ord("t"),ord("l"),ord("s"),ord("z"),ord("f"),ord("m"),ord("r"),\
    ord("e"),ord("h"),ord("d"),ord("p"),ord("x"),ord("k"),ord("i"),ord("b"),ord("v"),ord("y"),ord("g"), \
    ord("j"),ord("c"),ord("w"),ord("o"),ord("a")]

#getting message and storing to list as all lowercase
message = list(input("Input message:\n"))
message = [item.lower() for item in message]
print("Message = "+ str(message)+"\n")

encoded_message = []

#determining rotor order
all_rotors = ["I","II","III"]
string_rotor_order = list(input("Input rotor order separated by spaces:\n (options: I, II, III)"))
rotor_order = []
for item in string_rotor_order:
    if item not in all_rotors:
        print("Invalid selections")


#creating plug board key
board_key = input("Insert alphabet board key, characters separated only by spaces:\n").split()
board_key = [item.lower() for item in board_key]
print("Board key alpha = "+ str(board_key)+"\n")
board_key = [ord(item) for item in board_key]
print("Board key ord = "+str(board_key)+"\n")

"""
#ord("a") = 97
...
#ord("z") = 122
"""
"""
def plug_board(message,board_key):
    converted_message = []
    for letter in message:
        if letter.isalpha():
            converted_message.append(board_key[ord(letter)-97])
        else:
            converted_message.append(letter)
    return converted_message
"""

def plug_board(letter,board_key):
    converted_letter = 0
    converted_letter += board_key[ord(letter)-97]
    print(letter)
    print(chr(converted_letter))
    return converted_letter

#print(plug_board(message[0], board_key))

"""
def board_to_rotor(board_output):
    converted_message_ord = board_output
    converted_message_chr = []

    #converts converted_message_ord to chr characters without screwing up punctuation
    #stores indices of punctuation to punctuation_indices for re-insertion after rotors
    i = 0
    while i <= len(converted_message_ord)-1:
        for item in converted_message_ord:
            if type(item) == int:
                converted_message_chr.append(chr(item))
            else:
                converted_message_chr.append(item)
                punctuation_indices.append(i)
            i += 1
    ### for debugging purposes ###
    print("Original message = "+ str(message)+"\n")
    print("Plug board output = "+str(converted_message_ord)+"\n")
    print("Translated plug board output + "+str(converted_message_chr)+"\n")
    print("Indices of punctuation and spaces etc = "+ str(punctuation_indices)+"\n")
    print("")
    ### end debugging stuff ###
    converter_1_output = [item for item in converted_message_ord if type(item) == int]
    return converter_1_output
"""

def rotor_1(rotor,board_output):



#### CALLING FUNCTION CHAIN
for item in message:
    if item.isalpha():
        encoded_message.append((plug_board(item,board_key)))
    else:
        encoded_message.append(item)
#message_ord = [ord(item) for item in message]
#print(message_ord)
print(encoded_message)
