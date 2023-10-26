'''
generates randomised times tables for testing purposes

Dict keeps track of how often each question is asked so as to ensure even distribution of questions
'''
import sys
import os
import random


multiplier_list = []
multiplicand_range = range(2,13)

all_combinations = dict() 

#gather and sanitise user input. end result is a list of integers as the multipliers
print("Enter which times tables to include.")
print("Leave blank for default of 3,4,6,7,8,9,12")
user_input = input("Enter comma separated numbers: ")

if user_input == "":
    multiplier_list = [3, 4, 6, 7, 8, 9, 12]
else:
    multiplier_list = user_input.split(',')
    multiplier_list = [int(x) for x in multiplier_list if x.strip().isdigit()]

if len(multiplier_list) == 0:
    print("No valid input.  Exiting")
    sys.exit()
    
print(f'Testing on the following times tables: {multiplier_list}')
print('Press Enter to continue, or q to quit')

# build dict of all possible multiplier x multiplicant combinations as keys.  value = number of times it has been shown
for multiplier in multiplier_list:
    for multiplicant in multiplicand_range:
        multiplication_string = f'{multiplier} x {multiplicant}'
        all_combinations[multiplication_string] = 0

while True:
    #build list of keys that match lowest value
    lowest = list(all_combinations.values())
    lowest.sort()
    valid_keys = [key for key, value in all_combinations.items() if value == lowest[0]]
    
    #pick a random one and add 1 to its value
    random_choice = random.choice(valid_keys)
    all_combinations[random_choice] += 1

    #show expression and await for input
    print(random_choice)
    continue_input = input('')
    if continue_input == 'q':
        sys.exit()

    #clears screen for less messy viewing.  command depends on os.  does not work in IDLE but OK in py interpreter
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
    

