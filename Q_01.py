# 20099_Maniruzzaman_Md_HW1
# CS500(A)/HW1/Q_01
# Question: Python program that acts code-breaking device, translating letters into their corresponding digits...

    
def find_corresponding_code(character):     # function declare to get corresponding code/number from character
    
    corresponding_code_number = None
    if character in "ADGJM":
        corresponding_code_number = 1
    if character in "EFTUV":
        corresponding_code_number = 2
    if character in "BEKLO":
        corresponding_code_number = 3
    if character in "HSWXY":
        corresponding_code_number = 4
    if character in "CFNPQ":
        corresponding_code_number = 5
    if character in "IYZ":
        corresponding_code_number = 6
    if character in "HIRST":
        corresponding_code_number = 7
    if character in "Z":
        corresponding_code_number = 8
    return corresponding_code_number

def main():
    print("Enter a letter to decipher:")
    input_character = input("User input: ").upper()    # Input from keyboard by user and make it upper case
    
    if len(input_character)>1:                         # Error print, if input is not in single character
        print("Invalid input !, Please enter single character")
    else:
        corresponding_code_number = find_corresponding_code(input_character)
        
        if corresponding_code_number is not None:   # Output print for corret input and corresponding number
            print("Program output: You entered: ",input_character)
            print(f"The corresponding digit is ", corresponding_code_number,".")
        else:                                       # Output print if digits not exist
            print("Program output: You entered: ",input_character)
            print("No matching digit exists for this character.")

if __name__ == "__main__":
    main()