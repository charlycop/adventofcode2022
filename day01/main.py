filename = 'adventofcode/day01/inputs.txt'
max_calories_all = []

with open(filename, 'r') as handler:
    nb_lines = len(handler.readlines())
    handler.seek(0)
    max_calories_temp = 0
    
    for nb_line in range(nb_lines):
        line = handler.readline()
            
        if (len(line) == 1):
            max_calories_all.append(max_calories_temp)
            max_calories_temp = 0
            continue
        
        max_calories_temp += int(line)

max_calories_all.append(max_calories_temp) #for the last one
max_calories_all.sort()

print("Maximum calories of the first = ", max_calories_all[-1])
print("Maximum calories of the 3 firsts = ", max_calories_all[-1]+max_calories_all[-2]+max_calories_all[-3])