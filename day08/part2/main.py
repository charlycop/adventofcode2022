from enum import IntEnum
"""
   _____                _              _       
  / ____|              | |            | |      
 | |     ___  _ __  ___| |_ __ _ _ __ | |_ ___ 
 | |    / _ \| '_ \/ __| __/ _` | '_ \| __/ __|
 | |___| (_) | | | \__ \ || (_| | | | | |_\__ \
  \_____\___/|_| |_|___/\__\__,_|_| |_|\__|___/
"""
FILENAME        = 'adventofcode/day08/inputs.txt'
class Side(IntEnum):
   left      = 0
   right     = 1
   top       = 2
   bottom    = 3


"""
   _____ _       _           _     
  / ____| |     | |         | |    
 | |  __| | ___ | |__   __ _| |___ 
 | | |_ | |/ _ \| '_ \ / _` | / __|
 | |__| | | (_) | |_) | (_| | \__ \
  \_____|_|\___/|_.__/ \__,_|_|___/
"""                                                
datas            = []
nb_visible_trees = 0

"""
  ______                _   _                 
 |  ____|              | | (_)                
 | |__ _   _ _ __   ___| |_ _  ___  _ __  ___ 
 |  __| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
 | |  | |_| | | | | (__| |_| | (_) | | | \__ \
 |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
"""

def count_border_trees(datas):
    return (len(datas) * 2) + (len(datas[0]) * 2) - 4

def is_visible_left_right(side, ind_row, ind_col, datas, tree_size):
    nb_cols    = len(datas[0])
    ind_start  = 0
    ind_finish = 0

    if  side == Side.left :
        ind_start  = 0
        ind_finish = ind_col
    elif side == Side.right :
        ind_start  = ind_col+1
        ind_finish = nb_cols

    for i in range(ind_start,ind_finish) :
        neighbor_size = int(datas[ind_row][i])
        if neighbor_size >= tree_size : return False
            
    return True

def is_visible_top_bottom(side, ind_row, ind_col, datas, tree_size):
    nb_rows    = len(datas)
    ind_start  = 0
    ind_finish = 0

    if  side == Side.top :
        ind_start  = 0
        ind_finish = ind_row
    elif side == Side.bottom :
        ind_start  = ind_row+1
        ind_finish = nb_rows

    for i in range(ind_start, ind_finish):
        neighbor_size = int(datas[i][ind_col])
        if neighbor_size >= tree_size : return False
    
    return True

def is_tree_visible(ind_row, ind_col, datas):
    tree_size = int(datas[ind_row][ind_col])
    
    if   is_visible_left_right(Side.left,   ind_row, ind_col, datas, tree_size) : return True
    elif is_visible_left_right(Side.right,  ind_row, ind_col, datas, tree_size) : return True
    elif is_visible_top_bottom(Side.top,    ind_row, ind_col, datas, tree_size) : return True
    elif is_visible_top_bottom(Side.bottom, ind_row, ind_col, datas, tree_size) : return True
    
    return False


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

nb_rows       = len(datas)
nb_cols       = len(datas[0])

for row in range(1,nb_rows-1):
    for col in range(1,nb_cols-1) :
        if is_tree_visible(row, col, datas) : nb_visible_trees += 1

nb_visible_trees += count_border_trees(datas)

print("Number of trees visible from outside the grid :", nb_visible_trees)