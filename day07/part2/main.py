import sys # for sys.maxsize
"""
   _____                _              _       
  / ____|              | |            | |      
 | |     ___  _ __  ___| |_ __ _ _ __ | |_ ___ 
 | |    / _ \| '_ \/ __| __/ _` | '_ \| __/ __|
 | |___| (_) | | | \__ \ || (_| | | | | |_\__ \
  \_____\___/|_| |_|___/\__\__,_|_| |_|\__|___/
"""
FILENAME        = 'adventofcode/day07/inputs.txt'
ROOT            = 0
CD_CMD_POSITION = 1
CD_ARG_POSITION = 2
CD_COMMAND      = 'cd'
CD_ARG_ROOT     = '/'
CD_ARG_DOWN     = '..'
SIZE_POSITION   = 0
THRESHOLD       = 100000
CURRENT         = -1
SIZE            = 1
NAME            = 0
SIZE_ZERO       = 0
TOTAL_MEMORY    = 70000000
UNUSED_SPACE_TH = 30000000

"""
   _____ _       _           _     
  / ____| |     | |         | |    
 | |  __| | ___ | |__   __ _| |___ 
 | | |_ | |/ _ \| '_ \ / _` | / __|
 | |__| | | (_) | |_) | (_| | \__ \
  \_____|_|\___/|_.__/ \__,_|_|___/
"""                                                
datas = []
directories_dict     = {}
level_counter        = ROOT
folders_depth        = []
total_size           = 0
somme_size           = 0
numbers_of_folder    = 0

"""
  ______                _   _                 
 |  ____|              | | (_)                
 | |__ _   _ _ __   ___| |_ _  ___  _ __  ___ 
 |  __| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
 | |  | |_| | | | | (__| |_| | (_) | | | \__ \
 |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
"""
def is_a_size(line):
    size_str = line[0]
    return (ord(size_str[0]) > 47 and ord(size_str[0]) < 58)

# add a suffix to the folder name in case it's already in the dictionnary
def rename_dir_if_needed(folder):
    
    if (directories_dict.get(folder[NAME]) != None):
        try:   rename_dir_if_needed.counter += 1
        except AttributeError: rename_dir_if_needed.counter = 0
        folder[NAME] += '_' + str(rename_dir_if_needed.counter)

    return folder

def add_to_dictionnary(folder):
    child_folder = rename_dir_if_needed(folder)
    directories_dict[child_folder[NAME]] = child_folder[SIZE]      #record it into the final dictionnary
    folders_depth[CURRENT][SIZE] += child_folder[SIZE]             #add the size to the parent directory

def get_quickly_total_size(datas):
    quick_total_size = 0
    for line in datas:
        line = line.split()
        if is_a_size(line):
            quick_total_size += int(line[SIZE_POSITION])
    
    return quick_total_size

def get_quickly_unused_space(used_size):
    return TOTAL_MEMORY - used_size

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

for line in datas:
    line = line.split()

    if line[CD_CMD_POSITION] == CD_COMMAND:
        dest = line[CD_ARG_POSITION]
        
        if   dest == CD_ARG_ROOT : # initialisation
            level_counter = ROOT
            folders_depth.append([CD_ARG_ROOT, SIZE_ZERO]) 

        elif dest == CD_ARG_DOWN :
            level_counter -= 1
            add_to_dictionnary(folders_depth.pop())
        
        else : 
            level_counter += 1
            folders_depth.append([dest, SIZE_ZERO])
    
    elif is_a_size(line):
        size = int(line[SIZE_POSITION])
        folders_depth[CURRENT][SIZE] += size
        total_size                   += size

#to do the last one
add_to_dictionnary(folders_depth.pop())

# Search for folder to delete
unused_space = get_quickly_unused_space(total_size)
space_needed = UNUSED_SPACE_TH - unused_space

size_dir_to_delete = sys.maxsize

for dir_size in directories_dict.values():
    
    if space_needed == dir_size :
        size_dir_to_delete = dir_size
        break
    
    if space_needed < dir_size and dir_size < size_dir_to_delete :
        size_dir_to_delete = dir_size

print("The total size is : ", total_size)
print("Unused space =", unused_space, "- Space needed :", space_needed)
print("Size of the directory to delete = ", size_dir_to_delete)