
input = open('Inputs/Day_1_Input.txt').read().split()

#Part 1 
counter = 0
for i in range(1,len(input)):
    if int(input[i]) > int(input[i-1]):
        
        counter += 1
    
print(counter)

#Part 2
