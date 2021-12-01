
input = open('Inputs/Day_1_Input.txt').read().split()

#Part 1 
counter = 0
for i in range(1,len(input)):
    if int(input[i]) > int(input[i-1]):
        
        counter += 1
    
print("The answer to Part 1 is: " + str(counter))

#Part 2
counter = 0
Shift = 0

for i in range(0,len(input)-2,2):
    A = int(input[i]) + int(input[i+1]) + int(input[i+2])
    B = int(input[i+1]) + int(input[i+2]) + int(input[i+3])
    
    if A > Shift and Shift is not 0:
        counter += 1
    if B > A:
        counter += 1

    Shift = B    

print("The answer to Part 2 is: " + str(counter))
