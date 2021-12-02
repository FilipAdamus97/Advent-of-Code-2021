#Get Input
import time 
t0 = time.time() #Start Timer for comparison
input = open('Inputs/Day_2_Input.txt').read().split()

#Set Variables
h = 0 #Horizontal position
d = 0 #Depth

#Part 1
for x in range(0,len(input)-1,2):
    if input[x] == "forward":
        h += int(input[x+1])
    else: 
        if input[x] == "down":
            d += int(input[x+1])
        else: 
            if input[x] == "up":
                d -= int(input[x+1])

print("The answer to Part 1 is: " + str(h*d))

#Part 2 

#Set Variables
h = 0 #Horizontal position
d = 0 #Depth
aim = 0 #Aim

for x in range(0,len(input)-1,2):
    if input[x] == "forward":
        h += int(input[x+1])
        d += aim*int(input[x+1])
    else: 
        if input[x] == "down":
            aim += int(input[x+1])
        else: 
            if input[x] == "up":
                aim -= int(input[x+1])

print("The answer to Part 1 is: " + str(h*d))
t1 = time.time() #End timer for comaprison
total = t1-t0 #Calculate time of operation
print("Total time of operation: " + str(total))