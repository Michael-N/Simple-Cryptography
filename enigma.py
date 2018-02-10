import math
from datetime import datetime

#getting message and storing to list as all lowercase
message = list(input("Input message:\n"))
message = [item.lower() for item in message]
print("Message = "+ str(message)+"\n")
punctuation_indices = []

#creating plug board key
board_key = input("Insert alphabet board key, characters separated only by spaces:\n").split()
board_key = [item.lower() for item in board_key]
print("Board key alpha = "+ str(board_key)+"\n")
board_key = [ord(item) for item in board_key]
print("Board key ord = "+str(board_key)+"\n")

"""
ord("a") = 97
...
ord("z") = 122
"""

def plug_board(message,board_key):
    converted_message = []
    for letter in message:
        if letter.isalpha():
            converted_message.append(board_key[ord(letter)-97])
        else:
            converted_message.append(letter)
    return converted_message


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


def rotor_1(converter_1_output):

#### CALLING FUNCTION CHAIN
print(str(board_to_rotor(plug_board(message,board_key))))
