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
FILENAME         = 'day10/inputs.txt'
NB_CHAR_PER_LINE = 40
PIXEL_ON         = '#'
PIXEL_OFF        = '.'
CARRIAGE         = '\n'

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
crt_screen       = ""


"""
  ______                _   _                 
 |  ____|              | | (_)                
 | |__ _   _ _ __   ___| |_ _  ___  _ __  ___ 
 |  __| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
 | |  | |_| | | | | (__| |_| | (_) | | | \__ \
 |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
"""

def update_screen(cycle, center_sprite):
    pixel_pos     = (cycle-1) % NB_CHAR_PER_LINE

    global crt_screen
    if (pixel_pos >= center_sprite-1 and pixel_pos <= center_sprite+1):
           crt_screen += PIXEL_ON
    else : crt_screen += PIXEL_OFF
    
    if pixel_pos == NB_CHAR_PER_LINE-1 : crt_screen += CARRIAGE
    
def execute_instruction(instruc):
    
    cpu[cpu_.reg_X]    = cpu[cpu_.res_alu]
    cpu[cpu_.res_alu] += instruc[cmd.value]

    for i in range(cycles_needed[instruc[cmd.inst]]):
        cpu[cpu_.nb_cycles] += 1
        update_screen(cpu[cpu_.nb_cycles], cpu[cpu_.reg_X])

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

print(crt_screen)