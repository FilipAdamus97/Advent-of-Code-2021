from decimal import MAX_EMAX
import time

def part_1(input):

    startPoints = []
    endPoints = []
    helper = []

    for i in range(0,len(input),3):
        x, y = input[i].split(",")
        helper.append(x)
        helper.append(y)
        startPoints.append(helper)
        helper = []
        
        x, y = input[i+2].split(",")
        helper.append(x)
        helper.append(y)
        endPoints.append(helper)
        helper = []

    print(startPoints[0])
    print(endPoints[0])

    print(startPoints[1])
    print(endPoints[1])

    print(startPoints[2])
    print(endPoints[2])
    return "x"

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