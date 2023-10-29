'''
generates randomised times tables for testing purposes
Dict keeps track of how often each question is asked so as to ensure even distribution of questions
'''
import sys
import os
import random
import time

def clear():
    ''' creates universal clear screen command for console.  doesnt do anything in IDLE '''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_average_time(passed_dict):
    print('average time taken per expression:')
    for key, value in passed_dict.items():
        if len(value[2]) > 0:
            print('{0}: {1:.02} seconds over {2} attempts'.format(key, sum(value[2]) / len(value[2]), len(value[2])))

MULTIPLICAND_RANGE = range(2,13)

all_combinations = dict() 

#gather and sanitise user input. end result is a list of integers as the multipliers
clear()
print("Enter which times tables to include.")
print("Leave blank for default of 3,4,6,7,8,9,12")
user_input = input("Enter comma separated numbers: ")

if user_input == "":
    multiplier_list = [3, 4, 6, 7, 8, 9, 12]
else:
    multiplier_list = user_input.split(',')
    multiplier_list = [int(x) for x in multiplier_list if x.strip().isdigit()]

if len(multiplier_list) == 0:
    clear()
    print("No valid input.  Exiting")
    sys.exit()

# build dict of all possible multiplier x multiplicant combinations as keys.  value = number of times it has been shown
for multiplier in multiplier_list:
    for multiplicant in MULTIPLICAND_RANGE:
        multiplication_string = f'{multiplier} x {multiplicant}'
        
        all_combinations[multiplication_string] = [0, multiplier * multiplicant,[]]


while True:
    clear()
    print(f'Testing on the following times tables: {multiplier_list}')
    print('Press Enter to continue, or q to quit')
    print('')
    
    #build list of keys that match lowest value
    lowest = list(all_combinations.values())
    lowest.sort()
    valid_keys = [key for key, value in all_combinations.items() if value[0] == lowest[0][0]]
    
    #pick a random one and add 1 to its value
    random_choice = random.choice(valid_keys)
    all_combinations[random_choice][0] += 1

    #show expression and await for input
    print(random_choice)
    start_time = time.time()
    #print('')
    continue_input = input('')

    answer = all_combinations[random_choice][1]
    end_time = time.time()
  
    all_combinations[random_choice][2].append(end_time - start_time)
    if continue_input == 'q':
        clear()
        print_average_time(all_combinations)
        sys.exit()

    #flash the answer on the screen
    print(answer)

    time.sleep(0.5)
    

