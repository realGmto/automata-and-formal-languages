
dictionary = {"identifikatori": {},
              "separatori": {},
              "operatori": {}
              }
text = input("Enter your line:\n")

for letter in text:
    # Check if it is a indetificator
    if ord(letter) in range(ord('a'),ord('z')):
        print(f"('{letter}', identifikator)")
        dictionary['identifikatori'][letter]=dictionary.get('identifikatori',{}).get(letter,0)+1
    # Check if it is a operator
    elif letter in ['=','+','*']:
        print(f"('{letter}', operator)")
        dictionary['operatori'][letter]=dictionary.get('operatori',{}).get(letter,0)+1
    # Check if it is a separator
    elif letter == ' ':
        print(f"('{letter}', separator)")
        dictionary['separatori'][letter]=dictionary.get('separatori',{}).get(letter,0)+1

for outer_key,inner_dict in dictionary.items():
    print(f"{outer_key} [{sum(inner_dict.values())}]:", end=' ')
    print(", ".join("'{}'[{}]".format(key,value) for key,value in inner_dict.items()))