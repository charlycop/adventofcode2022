from enum import IntEnum

class Docks(IntEnum):
   firstelf_begin  = 0
   firstelf_end    = 1
   secondelf_begin = 2
   secondelf_end   = 3

filename = 'inputs.txt'
datas = []
somme = 0

def is_fully_contained(docks):
    return  (docks[Docks.firstelf_begin] >= docks[Docks.secondelf_begin] and docks[Docks.firstelf_end] <= docks[Docks.secondelf_end]) or (docks[Docks.secondelf_begin] >= docks[Docks.firstelf_begin] and docks[Docks.secondelf_end] <= docks[Docks.firstelf_end])

with open(filename, 'r') as handler:
    datas = handler.readlines()
    
for pairs in datas:
    docks = []
    pairs = pairs.split(',')        #first we remove the comma    
    for pair in pairs:
        pair = pair.split('-')      #then we remove the dash
        for dock in pair:
            docks.append(int(dock)) #finally we have a list with the 4 docks values
    
    if is_fully_contained(docks) : somme += 1 
    
print("There is", somme, "assignment pairs that does one range fully contain the other.")