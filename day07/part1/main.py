# declare constants 
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

# declare globals
datas = []
directories_dict     = {}
level_counter        = ROOT
folders_depth        = []
total_size           = 0
somme_size           = 0
numbers_of_folder    = 0

#Functions
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

#Getting the datas from the input file
with open(FILENAME, 'r') as handler:
    datas = handler.readlines()

# Program
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

for size in directories_dict.values():
    if size <= THRESHOLD : somme_size += size

print("The sum of the total sizes of of directories at most", THRESHOLD,"is :", somme_size)
print("The total size is : ", total_size)