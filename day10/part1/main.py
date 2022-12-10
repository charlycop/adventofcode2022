from enum import IntEnum

class cmd(IntEnum):
   inst     = 0
   value    = 1

class inst(IntEnum):
   noop     = 0
   addx     = 1

class cpu_(IntEnum):
   nb_cycles= 0
   reg_X    = 1
   res_alu  = 2

"""
   _____                _              _       
  / ____|              | |            | |      
 | |     ___  _ __  ___| |_ __ _ _ __ | |_ ___ 
 | |    / _ \| '_ \/ __| __/ _` | '_ \| __/ __|
 | |___| (_) | | | \__ \ || (_| | | | | |_\__ \
  \_____\___/|_| |_|___/\__\__,_|_| |_|\__|___/
"""
FILENAME        = 'day10/inputs.txt'

"""
   _____ _       _           _     
  / ____| |     | |         | |    
 | |  __| | ___ | |__   __ _| |___ 
 | | |_ | |/ _ \| '_ \ / _` | / __|
 | |__| | | (_) | |_) | (_| | \__ \
  \_____|_|\___/|_.__/ \__,_|_|___/
"""                                                
datas            = []
cpu              = [0, 1, 1]
cycles_needed    = {'addx':2, 'noop':1}
signal_strength  = {20:0, 60:0, 100:0, 140:0, 180:0, 220:0}

"""
  ______                _   _                 
 |  ____|              | | (_)                
 | |__ _   _ _ __   ___| |_ _  ___  _ __  ___ 
 |  __| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
 | |  | |_| | | | | (__| |_| | (_) | | | \__ \
 |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
"""
def get_sum_signal_strenght(signal_strenght_dict):
    somme = 0

    for value in signal_strenght_dict.values(): somme += value

    return somme

def get_signal_strenght (x_value, cyclecount):

    for cycle_target in signal_strength.keys():
        if cycle_target == cyclecount : 
            signal_strength[cycle_target] = cycle_target * x_value
            break

def execute_instruction(instruc):
    
    cpu[cpu_.reg_X]    = cpu[cpu_.res_alu]
    cpu[cpu_.res_alu] += instruc[cmd.value]

    for i in range(cycles_needed[instruc[cmd.inst]]):
        cpu[cpu_.nb_cycles] += 1
        get_signal_strenght(cpu[cpu_.reg_X], cpu[cpu_.nb_cycles])

def decode_instruction(line):
    line  = line.split()
    instr = [line[cmd.inst]]

    if   instr[cmd.inst] == 'addx' : instr.append(int(line[cmd.value]))
    elif instr[cmd.inst] == 'noop' : instr.append(0)

    return instr

""" 
  _____                                     
 |  __ \                                    
 | |__) | __ ___   __ _ _ __ __ _ _ __ ___  
 |  ___/ '__/ _ \ / _` | '__/ _` | '_ ` _ \ 
 | |   | | | (_) | (_| | | | (_| | | | | | |
 |_|   |_|  \___/ \__, |_|  \__,_|_| |_| |_|
                   __/ |                    
                  |___/   
"""
#Getting the datas from the input file
with open(FILENAME, 'r') as handler:
    datas = handler.readlines()

#cleaning the carriage return character
for i in range(len(datas)) : 
    if datas[i][-1] == '\n' : datas[i] = datas[i][:-1]

for line in datas:
    instr = decode_instruction(line)
    execute_instruction(instr)

print("Sum of the six signal strengths :", get_sum_signal_strenght(signal_strength))
print(cpu[cpu_.nb_cycles])