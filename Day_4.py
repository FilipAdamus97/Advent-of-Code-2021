import time
import numpy as np

def part_1(lottery_numbers, boards, markers):

    win = 0
    for i in lottery_numbers:
        for x in range(len(boards)):
            for y in range(len(boards[0])):
                for z in range(len(boards[0])):
                    if boards[x][y][z] == i:
                        markers[x][y][z] = 1

        for x in range(len(boards)):
            for y in range(len(boards[0])):
                if np.count_nonzero(markers[x][y]) == 5:
                    win = 1
            for y in range(len(boards[0])):
                if np.count_nonzero(markers[x][:][y]) == 5:
                    win = 1

    return "x"

def part_2(x):

    return "y"

def sort_input(x):

    lottery_numbers = []
    number_of_boards = int((len(x)-1)/25)
    boards = [np.zeros((5,5), dtype=int) for i in range(number_of_boards)]
    markers = [np.zeros((5,5), dtype=int) for i in range(number_of_boards)]
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
                boards[i][j][k] = int(np.float64(x[1+25*i+5*j+k]))
 
    return lottery_numbers, boards, markers

def main():
    input = open('Inputs/Day_4_Input.txt').read().split() #Get Input
    t0 = time.time() #Start Timer for comparison
    print("---------------------")
    
    #Part 1
    lottery_numbers, boards, markers = sort_input(input)
    print("Answer to Part 1 is " + str(part_1(lottery_numbers, boards, markers)))

    #Part 2
    print("Answer to Part 2 is " + str(part_2(input)))

    #Finishing touches
    t1 = time.time() #End timer for comaprison
    total = t1-t0 #Calculate time of operation
    print("Total time of operation: " + str(total))
    print("---------------------")

if __name__ == "__main__":
    main()