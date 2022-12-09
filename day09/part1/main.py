from enum import IntEnum

class Rope(IntEnum):
   H     = 0
   H_1   = 1
   T     = 2

class Motion(IntEnum):
   dir   = 0
   steps = 1

class Coord(IntEnum):
   X     = 0
   Y     = 1

"""
   _____                _              _       
  / ____|              | |            | |      
 | |     ___  _ __  ___| |_ __ _ _ __ | |_ ___ 
 | |    / _ \| '_ \/ __| __/ _` | '_ \| __/ __|
 | |___| (_) | | | \__ \ || (_| | | | | |_\__ \
  \_____\___/|_| |_|___/\__\__,_|_| |_|\__|___/
"""
FILENAME        = 'day09/inputs.txt'

"""
   _____ _       _           _     
  / ____| |     | |         | |    
 | |  __| | ___ | |__   __ _| |___ 
 | | |_ | |/ _ \| '_ \ / _` | / __|
 | |__| | | (_) | |_) | (_| | \__ \
  \_____|_|\___/|_.__/ \__,_|_|___/
"""                                                
datas            = []
visited_coord    = [[0, 0]]
last_position    = {Rope.H : [0, 0], Rope.H_1 : [0, 0], Rope.T : [0, 0]}

"""
  ______                _   _                 
 |  ____|              | | (_)                
 | |__ _   _ _ __   ___| |_ _  ___  _ __  ___ 
 |  __| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
 | |  | |_| | | | | (__| |_| | (_) | | | \__ \
 |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
"""
def move_H(direction, last_position):
    position_H              = last_position[Rope.H]

    # On enregistre l'ancienne position
    last_position[Rope.H_1] = [last_position[Rope.H][Coord.X], last_position[Rope.H][Coord.Y]]

    # On calcul la nouvelle position de H
    if   direction == 'L':
        position_H[Coord.X] -= 1
    elif direction == 'R':
        position_H[Coord.X] += 1
    elif direction == 'U':
        position_H[Coord.Y] += 1
    elif direction == 'D':
        position_H[Coord.Y] -= 1

def add_T_coord(position, visited):

    found = False

    for coord in visited:
        if (coord[Coord.X] == position[Coord.X]) and (coord[Coord.Y] == position[Coord.Y]):
            found = True
            break
    
    if not found : visited.append(position)

def move_T(last_position, visited):
    pos_H     = last_position[Rope.H]
    pos_H_1   = last_position[Rope.H_1]
    pos_T     = last_position[Rope.T]

    diff_H_T  = [pos_H[Coord.X] -   pos_T[Coord.X], pos_H[Coord.Y] -   pos_T[Coord.Y]]

    if   abs(diff_H_T[Coord.X]) > 1 or  abs(diff_H_T[Coord.Y]) > 1:
        last_position[Rope.T] = [pos_H_1[Coord.X], pos_H_1[Coord.Y]]
        add_T_coord(last_position[Rope.T], visited)


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

for motion in datas:
    motion    = motion.split()
    direction = motion[Motion.dir]
    nb_steps  = int(motion[Motion.steps])

    for step in range(nb_steps):
        move_H(direction, last_position)
        move_T(last_position, visited_coord)

print("Tail positions visited at least once :", len(visited_coord))