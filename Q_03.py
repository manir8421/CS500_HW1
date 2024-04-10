# 20099_Maniruzzaman_Md_HW1
# CS500(A)/HW1/Q_03
# Question: Python program that simulates the roll of a six-sided die, guided by the user's choices...


import random                          # random module for renarate random value

menu_input = ["1", "2", "3", "4"]      # define a list for menu option according to number

def dice():                                 # define funtion to take random generated number between 1 to 6
    random_number = random.randint(1, 6)
    return random_number

def stats(list_value,explosion):

    if list_value:
        n1 = n2 = n3 = n4 = n5 = n6 = 0     # roll state zero (0)
        count = len(list_value)

        for number in list_value:           # drive a loop for count number of rolls
            if number ==1:
                n1 += 1
            elif number ==2:
                n2 += 1
            elif number ==3:
                n3 += 1
            elif number ==4:
                n4 += 1
            elif number ==5:
                n5 += 1
            elif number ==6:
                n6 += 1

        print("Roll Statistics:")             # stats calculation according to output format
        print(f"Number 1: Rolled {n1} times ({((n1/count)*100):.2f}%)")
        print(f"Number 2: Rolled {n2} times ({((n2/count)*100):.2f}%)")
        print(f"Number 3: Rolled {n3} times ({((n3/count)*100):.2f}%)")
        print(f"Number 4: Rolled {n4} times ({((n4/count)*100):.2f}%)")
        print(f"Number 5: Rolled {n5} times ({((n5/count)*100):.2f}%)")
        print(f"Number 6: Rolled {n6} times ({((n6/count)*100):.2f}%) with {n6} explosions!")

    else:
        print("No Statistic, Pleae roll atleat once.")     # print if no any roll there

def show(list_value):                                      # count total number of rolls
    print(f"Total rolls made: ",len(list_value))

def input_data(keyboard):                                  # keyboard input vs menu list 
    return keyboard in menu_input

def main():                                                # menu list print

    print("Menu:")
    print("1. Roll Diac")
    print("2. View Total Rolls")
    print("3. View Roll Statistics")
    print("4. Exit")

    list_value = []                                    # counted roll value
    explosion = 0                                      # store counted number of explosions

    while True:
        keyboard = input("\nEnter your choice: ")       # User input from keyboard and checking conditions

        if input_data(keyboard):
            keyboard = int(keyboard)
        else:
            print("invalid input, Please entar choices from the menu.")
            continue

        dot = False
        if keyboard == 1:
            value_1 = dice()
            list_value.append(value_1)

            while value_1 == 6:                      # condition check for random number is 6
                print("You rolled a 6! The die explodes!")
                print("(Rolling again for explosion...)")
                value_1 = dice()

                if value_1 ==6:
                    explosion += 1                   # explosion count by increase value 1
                
                else:
                    dot = True
            print(f"You rolled a {value_1}!")

            if dot:                                    
                print("::")
                print("::")
        
        elif keyboard == 2:                             # call show function for input 2
            show(list_value)
        elif keyboard == 3:                             # call stats function for input 3
            stats(list_value,explosion)
        elif keyboard == 4:                             # break the loop if input 4
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()

