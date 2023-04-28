"""
1. Create a while loop that repeatedly takes user input and adds the input
to a list until the user enters \"done\
"""


def get_user_inputs():
    user_inputs = []
    while True:
        user_input = input("Enter a value: ")
        if user_input == 'done':
            break
        else:
            user_inputs.append(user_input)
    return user_inputs


"""
2. Create a while loop that generates random numbers and adds them to a list until 
the sum of all numbers in the list is greater than 100.
"""

import random

def random_hundred():
    randoms_sum = 0
    list_of_randoms = []
    while randoms_sum <= 100:
        num = random.randint(20, 30)
        if sum(list_of_randoms) + num <= 100:
            list_of_randoms.append(num)
            randoms_sum += num
        else:
            break
    return list_of_randoms

"""
Create a while loop that repeatedly takes user input and appends it to a list, 
but only if the input is a unique string."
"""
#I wouldn't use list here at all! That's a set functionality

def unique_input():
    inputs = []

    while True:
        user_input = input('Add your input (type "stop" to finish): ')
        if user_input == 'stop': #Must be condition to break out of the loop. "stop" won't be added to the list
            break
        if user_input not in inputs:
            inputs.append(user_input)

    return inputs

"""
4. Create a while loop that repeatedly takes user input and appends it to a list, 
but only if the input is a number greater than 10.
"""

def greater_ten():
    greater_ten_list = []
    while True:
        user_input = input('Enter your number (or type "stop" to finish): ')
        if user_input == 'stop':
            break
        try:
            if int(user_input) > 10:
                greater_ten_list.append(user_input)
            else:
                continue
        except ValueError:
            print("Enter numbers only!")
    return greater_ten_list

"""
5. Create a while loop that repeatedly takes user input and keeps track of the highest number entered 
 until the user enters \"done\".
"""

import sys
def highest_num():
    highest = -sys.maxsize - 1 #minInt
    first_run = True
    while True:
        user_input = input("Enter your number (or type 'done' to finish): ")
        if user_input == 'done':
            if first_run:
                return "You didn't type any number"
            break
        try:
            if int(user_input) > highest:
                highest = int(user_input)
            else:
                continue
        except ValueError:
            print("Enter integers only!")

        first_run = False
    return 'The highest number is:  ' + str(highest)


if __name__ == '__main__':
    #print(get_user_inputs())
    #print(random_hundred())
    #print(unique_input())
    #print(greater_ten())
    print(highest_num())
