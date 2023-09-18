
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(input_str, shift):
    output = ""
    for i in input_str.lower():
        new_alpha_val = abs( alphabet.index(i) + shift ) % 26
        output += alphabet[new_alpha_val]
    return output
def decode(input_str, shift):
    output = ""
    for i in input_str.lower():
        new_alpha_val = ( alphabet.index(i) - shift ) % 26
        output += alphabet[new_alpha_val]
    return output



print(""" .o88b.  .d8b.  d88888b .d8888.  .d8b.  d8888b. 
d8P  Y8 d8' `8b 88'     88'  YP d8' `8b 88  `8D 
8P      88ooo88 88ooooo `8bo.   88ooo88 88oobY' 
8b      88~~~88 88~~~~~   `Y8b. 88~~~88 88`8b   
Y8b  d8 88   88 88.     db   8D 88   88 88 `88. 
 `Y88P' YP   YP Y88888P `8888Y' YP   YP 88   YD 
                                                
                                                
 .o88b. d888888b d8888b. db   db d88888b d8888b. 
d8P  Y8   `88'   88  `8D 88   88 88'     88  `8D 
8P         88    88oodD' 88ooo88 88ooooo 88oobY' 
8b         88    88~~~   88~~~88 88~~~~~ 88`8b   
Y8b  d8   .88.   88      88   88 88.     88 `88. 
 `Y88P' Y888888P 88      YP   YP Y88888P 88   YD""")
e_or_d = input("'encode' or 'decode':\n")
message = input("Type your message:\n")
shift_number = int(input("Type the shift number:\n"))
if e_or_d == "encode":
    output = encode(message, shift_number)
else:
    output = decode(message, shift_number)
print(f"Here's the encoded result: {output}")