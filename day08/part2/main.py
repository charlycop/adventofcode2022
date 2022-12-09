from enum import IntEnum
"""
   _____                _              _       
  / ____|              | |            | |      
 | |     ___  _ __  ___| |_ __ _ _ __ | |_ ___ 
 | |    / _ \| '_ \/ __| __/ _` | '_ \| __/ __|
 | |___| (_) | | | \__ \ || (_| | | | | |_\__ \
  \_____\___/|_| |_|___/\__\__,_|_| |_|\__|___/
"""
FILENAME        = 'day08/inputs.txt'

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
datas             = []
best_scenic_score = 0

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

def nb_visible_left_right(side, ind_row, ind_col, datas, tree_size):
    nb_cols      = len(datas[0])
    ind_start    = 0
    ind_finish   = 0
    trees_viewed = 0
    increment    = 0

    if  side == Side.left :
        ind_start    = ind_col-1
        ind_finish   = -1
        increment    = -1
    elif side == Side.right :
        ind_start    = ind_col+1
        ind_finish   = nb_cols
        increment    = 1

    for i in range(ind_start,ind_finish, increment) :
        neighbor_size = int(datas[ind_row][i])
        trees_viewed += 1
        if neighbor_size >= tree_size :
            break
            
    return trees_viewed

def nb_visible_top_bottom(side, ind_row, ind_col, datas, tree_size):
    nb_rows      = len(datas)
    ind_start    = 0
    ind_finish   = 0
    trees_viewed = 0
    increment    = 0

    if  side == Side.top :
        ind_start  = ind_row-1
        ind_finish = -1
        increment  = -1
    elif side == Side.bottom :
        ind_start  = ind_row+1
        ind_finish = nb_rows
        increment  = 1

    for i in range(ind_start, ind_finish, increment):
        neighbor_size = int(datas[i][ind_col])
        trees_viewed += 1
        if neighbor_size >= tree_size :
                break
    
    return trees_viewed

def get_scenic_score(ind_row, ind_col, datas):
    tree_size    = int(datas[ind_row][ind_col])

    scenic_score  = nb_visible_left_right(Side.left,   ind_row, ind_col, datas, tree_size)
    scenic_score *= nb_visible_left_right(Side.right,  ind_row, ind_col, datas, tree_size)
    scenic_score *= nb_visible_top_bottom(Side.top,    ind_row, ind_col, datas, tree_size)
    scenic_score *= nb_visible_top_bottom(Side.bottom, ind_row, ind_col, datas, tree_size)
    
    return scenic_score


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

nb_rows           = len(datas)
nb_cols           = len(datas[0])

for row in range(1,nb_rows-1):
    for col in range(1,nb_cols-1) :
        scenic_tree_score = get_scenic_score(row, col, datas)
        if scenic_tree_score > best_scenic_score:
            best_scenic_score = scenic_tree_score

print("The best scenic score is :", best_scenic_score)