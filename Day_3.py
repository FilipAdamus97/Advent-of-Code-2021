import time 

def main():
    t0 = time.time() #Start Timer for comparison
    print("---------------------")
    input = open('Inputs/Day_3_Input.txt').read().split() #Get Input

    #Part 1
    print("Answer to Part 1 is " + str(Calculate_Gamma_Epsilon(input)))

    #Part 2
    print("Answer to Part 2 is " + str(Calculate_Life_Support(input)))

    #Finishing touches
    t1 = time.time() #End timer for comaprison
    total = t1-t0 #Calculate time of operation
    print("Total time of operation: " + str(total))
    print("---------------------")

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
    
    return int(Gamma_Rate, 2) * int(Epsilon_Rate, 2)

def Calculate_Life_Support(x):

    oxygen, co2 = x.copy(), x.copy()

    #Oxygen
    counter = 0
    j = 0
    while len(oxygen)>1:
        placeholder = []
        for i in oxygen:
            if int(i[j]) == 1:   
                counter += 1
        if counter >= len(oxygen)/2:
            most_common = "1"
        else:
            most_common = "0"
        for i in oxygen:
            if i[j] is most_common:
                placeholder.append(i)
        oxygen = placeholder
        counter = 0
        j += 1
    
    #CO2
    counter = 0
    j = 0
    while len(co2)>1:
        placeholder = []
        for i in co2:
            if int(i[j]) == 1:   
                counter += 1
        if counter >= len(co2)/2:
            most_common = "1"
        else:
            most_common = "0"
        for i in co2:
            if i[j] is not most_common:
                placeholder.append(i)
        co2 = placeholder
        counter = 0
        j += 1

    return int(oxygen[0], 2) * int(co2[0], 2)

if __name__ == "__main__":
    main()