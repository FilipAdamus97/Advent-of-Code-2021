import time

def part_1(x):

    return "x"

def part_2(x):

    return "y"

def main():
    t0 = time.time() #Start Timer for comparison
    input = open('Inputs/Day_4_Input.txt').read().split() #Get Input

    print(input[0])
    print(input[1])
    print(input[2])

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