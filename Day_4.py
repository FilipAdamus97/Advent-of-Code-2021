import time
import numpy as np

def part_1(x):

    return "x"

def part_2(x):

    return "y"

def sort_input(x):

    lottery_numbers = []
    number_of_boards = int((len(x)-1)/25)
    boards = [np.zeros((5,5)) for i in range(number_of_boards)]
    markers = boards.copy()
    placeholder = ''
    

    for i in x[0]:
        if i is not ',':
            placeholder += i
        else:
            lottery_numbers.append(int(placeholder))
            placeholder = ''

    for i in range(number_of_boards):
        for j in range(5):
            for k in range(5):
                boards[i][j][k] =  int(x[1+25*i+5*j+k]) 
 
    return lottery_numbers, boards, markers

def main():
    input = open('Inputs/Day_4_Input.txt').read().split() #Get Input
    t0 = time.time() #Start Timer for comparison
    print("---------------------")
    lottery_numbers, boards, markers = sort_input(input)
    #Part 1
    print("Answer to Part 1 is " + str(part_1(input)))

    #Part 2
    print("Answer to Part 2 is " + str(part_2(input)))

    #Finishing touches
    t1 = time.time() #End timer for comaprison
    total = t1-t0 #Calculate time of operation
    print("Total time of operation: " + str(total))
    print("---------------------")

if __name__ == "__main__":
    main()