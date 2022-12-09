from enum import IntEnum

class Node(IntEnum):
   H     = 0
   T     = 9

class Motion(IntEnum):
   dir   = 0
   steps = 1

class Coord(IntEnum):
   X     = 0
   Y     = 1
   X_bef = 2
   Y_bef = 3

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
last_position    = [[0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]]


"""
  ______                _   _                 
 |  ____|              | | (_)                
 | |__ _   _ _ __   ___| |_ _  ___  _ __  ___ 
 |  __| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
 | |  | |_| | | | | (__| |_| | (_) | | | \__ \
 |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
"""
def move_H(direction, last_position):
    position_H = last_position[Node.H]

    # On enregistre l'ancienne position
    last_position[Node.H][Coord.X_bef] = position_H[Coord.X]
    last_position[Node.H][Coord.Y_bef] = position_H[Coord.Y]

    # On calcul la nouvelle position de H
    if   direction == 'L': position_H[Coord.X] -= 1
    elif direction == 'R': position_H[Coord.X] += 1
    elif direction == 'U': position_H[Coord.Y] += 1
    elif direction == 'D': position_H[Coord.Y] -= 1

def add_T_coord(position, visited):

    found = False

    for coord in visited:
        if (coord[Coord.X] == position[Coord.X]) and (coord[Coord.Y] == position[Coord.Y]):
            found = True
            break
    
    if not found : visited.append(position[:Coord.X_bef])

def move_Others(node, last_position, visited):
    pos_node_prec       = last_position[node-1]
    pos_node            = last_position[node]

    diff_H_T     = [pos_node_prec[Coord.X] - pos_node[Coord.X], pos_node_prec[Coord.Y] - pos_node[Coord.Y]]
    abs_diff_H_T = [abs(diff_H_T[Coord.X]), abs(diff_H_T[Coord.Y])]

    # si on a pas une différence d'au moins 2 on sort tout de suite
    if abs_diff_H_T[Coord.X] < 2 and abs_diff_H_T[Coord.Y] < 2:
        return

    # On backup l'ancienne position avant de la modifier
    pos_node[Coord.X_bef] = pos_node[Coord.X]
    pos_node[Coord.Y_bef] = pos_node[Coord.Y]
    
    # Si un des deux est egal a zero alors c'est une translation horizontal ou vertical
    if   diff_H_T[Coord.Y] == 0 or diff_H_T[Coord.X] == 0 :
        if   diff_H_T[Coord.X] ==  2 : pos_node[Coord.X] += 1
        elif diff_H_T[Coord.X] == -2 : pos_node[Coord.X] -= 1
        elif diff_H_T[Coord.Y] ==  2 : pos_node[Coord.Y] += 1
        elif diff_H_T[Coord.Y] == -2 : pos_node[Coord.Y] -= 1

    elif abs_diff_H_T[Coord.Y] == 1 : #implicit abs_diff_H_T[Coord.X] == 2
        
        pos_node[Coord.Y] +=  diff_H_T[Coord.Y]
        if diff_H_T[Coord.X] > 0 : pos_node[Coord.X]  +=  1
        else :                     pos_node[Coord.X]  -=  1
    
    elif abs_diff_H_T[Coord.X] == 1 : #implicit abs_diff_H_T[Coord.Y] == 2
        
        pos_node[Coord.X] += diff_H_T[Coord.X]
        if diff_H_T[Coord.Y] > 0 : pos_node[Coord.Y] +=  1
        else :                     pos_node[Coord.Y] -=  1

    # Finalement: Si on a les deux coordonnées au dela de 1
    else: 
        if diff_H_T[Coord.X] > 0 : pos_node[Coord.X]  += 1
        else:                      pos_node[Coord.X]  -= 1
        
        if diff_H_T[Coord.Y] > 0 : pos_node[Coord.Y]  += 1
        else:                      pos_node[Coord.Y]  -= 1

    # On enregistre la position de la queue si elle n'existe pas déjà
    if node == Node.T : add_T_coord(pos_node, visited)


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
        for node in range(Node.H+1,len(last_position)):
            move_Others(node, last_position, visited_coord)

print("Tail positions visited at least once :", len(visited_coord))