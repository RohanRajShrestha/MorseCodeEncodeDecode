MORSE_CODE = (
    ("-...", "B"), (".-", "A"), ("-.-.", "C"), ("-..", "D"), (".", "E"), ("..-.", "F"), ("--.", "G"),
    ("....", "H"), ("..", "I"), (".---", "J"), ("-.-", "K"), (".-..", "L"), ("--", "M"), ("-.", "N"),
    ("---", "O"), (".--.", "P"), ("--.-", "Q"), (".-.", "R"), ("...", "S"), ("-", "T"), ("..-", "U"),
    ("...-", "V"), (".--", "W"), ("-..-", "X"), ("-.--", "Y"), ("--..", "Z"), (".-.-.-", "."),
    ("-----", "0"), (".----", "1"), ("..---", "2"), ("...--", "3"), ("....-", "4"), (".....", "5"), 
    ("-....", "6"), ("--...", "7"), ("---..", "8"), ("----.", "9"), ("-.--.", "("), ("-.--.-", ")"),
    (".-...", "&"), ("---...", ":"), ("-.-.-.", ";"), ("-...-", "="), (".-.-.", "+"), ("-....-", "-"),
    ("..--.-", "_"), (".-..-.", '"'), ("...-..-", "$"), (".--.-.", "@"), ("..--..", "?"), ("-.-.--", "!")
)

def print_intro():
    print("Welcome to Wolmorse")
    print("This program encodes and decodes Morse code.")

def get_input():
    inp = input("Would you like to encode (e) or decode (d): ")
    if inp == "e":
        encode_msg = input("What message would you like to encode: ")
        return encode(encode_msg)
    elif inp == "d":
        decode_msg = input("What message would you like to decode: ")
        return decode(decode_msg)
    else:
        print("Invalid Input")
        return get_input()

def encode(message):
    my_list = []

    my_list = list(message.upper()) 
    # list banauna string lai
    # print(my_list)
    my_letter = ""
    # MORSE_CODE[0][1]
    my_string = ''
    for my_letter in my_list:
        i = 0
        if my_letter != ' ':
            while i < len(MORSE_CODE):
                if my_letter == MORSE_CODE[i][1]:
                    my_string += MORSE_CODE[i][0] + ' '
                    break
                i += 1
        else:
            my_string += '   '
    print(my_string)
    return decision()

def decode(message):
    my_list = []
    my_list = message.split(' ')
    decode_code = ""
    
    for morse_code in my_list:
        i = 0
        if morse_code != "":
            while i < len(MORSE_CODE):
                if morse_code == MORSE_CODE[i][0]:
                    decode_code += MORSE_CODE[i][1];
                    break
                i += 1
        else:
            decode_code += " "

    print(decode_code.replace("  ", "")) 
    return decision()

def decision():
    decide = input("Would you like to encode/decode another message? (y/n):")
    if decide == "y":
        return get_input()
    elif decide == "n":
        print("Thanks for using the program, goodbye!")
    else:
        print("Invalid Input")
        return decision()
print_intro()
get_input()

# Would you like to encode/decode another message? (y/n): n
# Thanks for using the program, goodbye!


# a = "hello world"

# my_list = []

# my_list = list(a.upper()) 
# # list banauna string lai
# # print(my_list)
# my_letter = ""
# # MORSE_CODE[0][1]
# my_string = ''

# for my_letter in my_list:
#     i = 0
#     if my_letter != ' ':
#         while i < len(MORSE_CODE):
#             if my_letter == MORSE_CODE[i][1]:
#                 my_string += MORSE_CODE[i][0] + ' '
#                 break
#             i += 1
#     else:
#         my_string += ' '
#     # loop samapta
# print(my_string)

# print(my_string.split(' '))

# def print_intro():
#     print("enter value: ")
#     return get_input(a)

# def    get_input():
#     if input == e:
#         encode(message)
#     else:
#         decode(message)


# def encode(message):
#     pass


# def decode(message):
            

