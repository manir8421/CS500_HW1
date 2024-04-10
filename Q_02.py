# 20099_Maniruzzaman_Md_HW1
# CS500(A)/HW1/Q_02
# Question: Python program that checks whether a given five-character string is a palindrome...


def palindrome_check(input_word):   # function declare for plaindrome and replace position and latter

    x = True                        # initialize a boolean variable for check plaindrome
    a = 0                           # variable for start index
    b = len(input_word) - 1         # variable for end index
    pos = None                      # variable for store position
    ltr = None                      # variable for store latter for replace
    flg = 0                         # variable for counting non-matching
    
    while a<b:
        if input_word[a]!=input_word[b]:
            x = False
            pos = a + 1
            ltr = input_word[b]     # store the latter for replace
            flg += 1                # non-matching count
        a += 1
        b -= 1
    
    if flg > 1:
        pos,ltr = None, None
    
    return x, pos, ltr              # return the result to function

    
def rev(input_word,pos,ltr):    # function declare for keyboard/user input and make a reversed string of input
    rev_word = " "                  # empty string for reversed word store
    for a in range(len(input_word)):
        if a == pos-1:
            rev_word += ltr
        else:
            rev_word += input_word[a]
    return rev_word.upper()         # makeupper case of the reversed word

def main():                       # main function declare

    input_word = input(" Enter a five-character string: ")
    if len(input_word)>5:
       print("Error: Invalid input: Please enter a five-character string.")
       input_word = input("Enter a five-character string: ")
    
    rev_word= " "
    pln, pos, ltr = palindrome_check(input_word) # function call and store result & print output
    if pos:
       rev_word = rev(input_word,pos,ltr)
    result = " "
    if pln:
        print("It is palindrome")
    else:
        if pos:
            result += (f"{input_word} is not a palindrome. Replace character {pos} with '{ltr}' to make it a palindrome.\n Revised string with uppercase: {rev_word}")
        else:
            result += (f"{input_word} is not a palindrome. No single character replacement can make it one.")
        print(result)


if __name__ == "__main__":
    main()