from decimal import MAX_EMAX
import numpy as np
import time

def part_1(input):

    start = [] #List of x1,y1 elements
    end = [] #List of x2,y2 elements
    counter = 0 #Final Answer for Part 1
    helper = [] 

    for i in range(0,len(input),3):
        x, y = input[i].split(",")
        helper.append(int(x))
        helper.append(int(y))
        start.append(helper)
        helper = []
        
        x, y = input[i+2].split(",")
        helper.append(int(x))
        helper.append(int(y))
        end.append(helper)
        helper = []


    field = np.zeros((1000,1000)) # Matrix with the whole map of the region
#aaa

    # Horizontal and Vertical lines only
    for i in range(len(start)): # For every line in Input
        # If line is horizontal (X is the same) 
        if start[i][0] == end[i][0] and end[i][1] > start[i][1]: # If X is constant and Y is increasing
            for j in range(start[i][1],end[i][1]):
                field[start[i][0]][j+1] += 1
        elif start[i][0] == end[i][0] and end[i][1] < start[i][1]: # If X is constant and Y is decreasing
            for j in range(end[i][1],start[i][1],-1):
                field[start[i][0]][j-1] += 1

        # If line is Vertical (Y is the same)
        if start[i][1] == end[i][1] and end[i][0] > start[i][0]: # If Y is constant and X is increasing
            for j in range(start[i][0],end[i][0]):
                field[j+1][start[i][1]] += 1
        elif start[i][1] == end[i][1] and end[i][0] < start[i][0]: # If Y is constant and X is decreasing
            for j in range(end[i][0],start[i][0],-1):
                field[j-1][start[i][1]] += 1
    


    for i in range(len(field[:][0])):
        for j in range(len(field[0][:])):
            if field[i][j] > 1:
                counter += 1
    return counter

def part_2(x):

    return "y"

def main():
    t0 = time.time() #Start Timer for comparison
    input = open('Inputs/Day_5_Input.txt').read().split() #Get Input

    print("---------------------")

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