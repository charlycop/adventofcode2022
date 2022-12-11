"""
   _____                _              _       
  / ____|              | |            | |      
 | |     ___  _ __  ___| |_ __ _ _ __ | |_ ___ 
 | |    / _ \| '_ \/ __| __/ _` | '_ \| __/ __|
 | |___| (_) | | | \__ \ || (_| | | | | |_\__ \
  \_____\___/|_| |_|___/\__\__,_|_| |_|\__|___/
"""
FILENAME          = 'day11/inputs.txt'
#FILENAME           = 'day11/inputs_tests.txt'
nb_line_per_moneys = 7

"""
   _____ _       _           _     
  / ____| |     | |         | |    
 | |  __| | ___ | |__   __ _| |___ 
 | | |_ | |/ _ \| '_ \ / _` | / __|
 | |__| | | (_) | |_) | (_| | \__ \
  \_____|_|\___/|_.__/ \__,_|_|___/
"""                                                
datas            = []
monkeys          = []
nb_rounds        = 10000
ppcm             = 0

"""
  ______                _   _                 
 |  ____|              | | (_)                
 | |__ _   _ _ __   ___| |_ _  ___  _ __  ___ 
 |  __| | | | '_ \ / __| __| |/ _ \| '_ \/ __|
 | |  | |_| | | | | (__| |_| | (_) | | | \__ \
 |_|   \__,_|_| |_|\___|\__|_|\___/|_| |_|___/
"""

def karatsuba(m,n):
    if(m<10 or n<10):
        return m*n
    else:
        mstring = str(m)
        nstring = str(n)
        k = max(len(mstring), len(nstring))
        mid=int(k/2)
            #finding a and c i.e. the higher bits for each number
        a = int(mstring[:-mid])
        c = int(nstring[:-mid])
            #finding b and d i.e. the lower bits for each number
        b = int(mstring[-mid:])
        d = int(nstring[-mid:])
            #finding ac, bd and ad_plus_bc
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a + b, c + d) - ac - bd
        return ac*10**(2 * mid) + ad_plus_bc*10**(mid) + bd

def reduce_worry2(x): # part 2 
    return x % ppcm 

def clean_convert_items(dirty_items):
    clean_items = []
    for dirty_item in dirty_items:
        clean_item = dirty_item
        if dirty_item[-1] == ',':
            clean_item = clean_item[:-1]
        
        clean_items.append(int(clean_item))
    
    return clean_items

def find_two_most_active():
    most_actives = []
    inspected_elements = []

    for monkey in monkeys:
        inspected_elements.append(monkey['inspected_items'])
    
    for i in range(2):
        ind_max = find_most_active(inspected_elements)
        most_actives.append(inspected_elements.pop(ind_max))
    
    return most_actives

        
def find_most_active(inspected_numbers):
    max_ind = 0
    max_val = 0
    for i in range(len(inspected_numbers)):
        if inspected_numbers[i] > max_val :
            max_val = inspected_numbers[i]
            max_ind = i
    
    return max_ind


def parse_datas(datas):
    for line in range(1, len(datas), nb_line_per_moneys) :
        monkey_input = datas[line:line+nb_line_per_moneys-2]
        monkey_dict = {}

        for sub_line in monkey_input:
            sub_line = sub_line.split()
         
            if   sub_line[0] == 'Starting': 
                monkey_dict['items'] = clean_convert_items(sub_line[2:])

            elif sub_line[0] == 'Operation:':
                monkey_dict['oper']     = sub_line[4]
                monkey_dict['oper_val'] = sub_line[5]

            elif sub_line[0] == 'Test:' :
                monkey_dict['test'] = int(sub_line[3])

            elif sub_line[1] == 'true:' :
                monkey_dict['outcome'] = int(sub_line[5])

            elif sub_line[1] == 'false:' :
                monkey_dict['outcome'] = [monkey_dict['outcome'], int(sub_line[5])]

            monkey_dict['inspected_items'] = 0

        global monkeys
        monkeys.append(monkey_dict)

def get_dividors():
    dividors = []

    for monkey in monkeys:
        dividors.append(int(monkey['test']))
    
    return dividors
    
def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

def compute_lcm_many(numbers):
    res = numbers[0]
    for i in range(1,len(numbers)):
        res = compute_lcm(res, numbers[i])
    return res

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

parse_datas(datas)

ppcm = compute_lcm_many(get_dividors())

for round in range(nb_rounds):
    for i in range(0, len(monkeys)):
        monkey    = monkeys[i]
        len_items = len(monkey['items'])
        for j in range(len_items):
            monkey['inspected_items'] += 1
            worry_item = monkey['items'].pop(0)
            oper_val   = worry_item if monkey['oper_val'] == 'old' else int(monkey['oper_val'])
            
            if   monkey['oper'] == '+' : worry_item += oper_val
            elif monkey['oper'] == '*' : worry_item *= oper_val

            worry_item = reduce_worry2(worry_item)

            target_monkey = 0 if worry_item % monkey['test'] == 0 else 1
            monkeys[monkey['outcome'][target_monkey]]['items'].append(worry_item)
           

most_actives_monkeys = find_two_most_active()

print("== After round",nb_rounds,"==")
for i in range(len(monkeys)):
    print("Monkey", i, "inspected items", monkeys[i]['inspected_items'], "times.")    
print("The level of monkey business is : ", most_actives_monkeys[0]*most_actives_monkeys[1])