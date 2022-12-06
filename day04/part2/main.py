from enum import IntEnum

class Docks(IntEnum):
   firstelf_begin  = 0
   firstelf_end    = 1
   secondelf_begin = 2
   secondelf_end   = 3

filename = 'inputs.txt'
datas = []
somme = 0

def is_overlapping(docks):

    for dockfirst in range (docks[Docks.firstelf_begin], docks[Docks.firstelf_end]+1):
        for docksecond in range (docks[Docks.secondelf_begin], docks[Docks.secondelf_end]+1):
            if dockfirst == docksecond: return True
                
    return False

with open(filename, 'r') as handler:
    datas = handler.readlines()
    
for pairs in datas:
    docks = []
    pairs = pairs.split(',')        #first we remove the comma    
    for pair in pairs:
        pair = pair.split('-')      #then we remove the dash
        for dock in pair:
            docks.append(int(dock)) #finally we have a list with the 4 docks values
    
    if is_overlapping(docks) : somme += 1 
    
print("There is", somme, "assignment pairs doing the ranges overlap.")