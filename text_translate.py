#This code can translate from Alphanumeric to Binary, or vice versa

#Dictionaries
DNA_dictionary = {
    "00": "A",
    "10": "G",
    "01": "C",
    "11": "T"
} 

Binary_dictionary = {
    "A": "00",
    "G": "10",
    "C": "01",
    "T": "11"
}

output = ''
binary = ''
input_text = ''

Translation_type = input("Would you like to translate to or from DNA (to/from): ")


def toDNA():
    binary = ''.join(format(ord(i), '08b') for i in input_text)
 
    binary_2bit = [
    binary[x:x+2] for x in range(0, len(binary), 2)
    ]

    DNA_list = []

    for y in binary_2bit:
        for z in list(DNA_dictionary.keys()):
            if y == z:
                DNA_list.append(DNA_dictionary.get(z))

    output = "".join(DNA_list)
    return output, binary

def fromDNA():
    DNA_1bit = [
        input_text[x:x+1] for x in range(0, len(input_text))
    ]
    
    binary_list = []
    
    for y in DNA_1bit:
        for z in list(Binary_dictionary.keys()):
            if y == z:
                binary_list.append(Binary_dictionary.get(z))
    
    binary_data = ''.join(binary_list)
    output = ''.join(chr(int(binary_data[i*8:i*8+8], 2)) for i in range(len(binary_data)//8))
    return output, binary_data

if Translation_type == 'to':
    input_text = input("What do you want to translate?: ")
    output, binary = toDNA()
    print("Here is your original message: " + str(input_text))
    print("Here is your original string in binary: " + str(binary))
    print("Here is your translated DNA string: " + str(output))

elif Translation_type == 'from':
    input_text = input("What do you want to translate?: ")
    output, binary = fromDNA()
    print("Here is your original DNA string: " + str(input_text))
    print("Here is your original string in binary: " + str(binary))
    print("Here is your translated message: " + str(output))

else:
    print("that's not a valid option ￣へ￣")
    print("please run the program again")
    quit()








