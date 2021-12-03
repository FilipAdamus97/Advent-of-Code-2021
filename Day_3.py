import time 

def main():
    t0 = time.time() #Start Timer for comparison
    input = open('Inputs/Day_3_Input.txt').read().split() #Get Input

    #Part 1
    Gamma_Rate, Epsilon_Rate = Calculate_Gamma_Epsilon(input)
    print("Answer to Part 1 is " + str(Gamma_Rate * Epsilon_Rate))

    #Part 2

    t1 = time.time() #End timer for comaprison
    total = t1-t0 #Calculate time of operation
    print("Total time of operation: " + str(total))

def Calculate_Gamma_Epsilon(x):
    Gamma_Rate, Epsilon_Rate = "", "" 
    counter_1 = [0 for x in range(len(x[0]))]
    for i in range(len(x)):
        for j in range(len(x[0])):
            if int(x[i][j]) == 1 :
                counter_1[j] += 1       
       
    for i in counter_1:
        if i > 500:
            Gamma_Rate += "1"
            Epsilon_Rate += "0"
        else: 
            Gamma_Rate += "0"
            Epsilon_Rate += "1"
    
    return int(Gamma_Rate, 2), int(Epsilon_Rate, 2)


if __name__ == "__main__":
    main()