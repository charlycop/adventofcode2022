from enum import IntEnum

filename         = 'inputs.txt'
shape_points     = {"X" : 1, "Y" : 2, "Z" : 3}
outcome_decode   = {"X" : "lost", "Y" : "draw", "Z" : "won"}
outcome_points   = {"won" : 6, "draw" : 3, "lost" : 0}
shape_opp_to_moi = {"A" : "X", "B" : "Y", "C" : "Z"}
points = []

class data(IntEnum):
   outcome        = 2
   opponent_shape = 0
    
def get_my_shape(outcome_encoded, shape_opponent):
    shape_moi = ""
    outcome = outcome_decode[outcome_encoded]
    
    if   outcome == "draw":
        shape_moi = shape_opp_to_moi[shape_opponent]
    
    elif outcome == "lost":
        if   shape_opponent == "A": shape_moi = "Z"
        elif shape_opponent == "B": shape_moi = "X"
        elif shape_opponent == "C": shape_moi = "Y"
    
    elif outcome == "won":
        if   shape_opponent == "A": shape_moi = "Y"
        elif shape_opponent == "B": shape_moi = "Z"
        elif shape_opponent == "C": shape_moi = "X"
    
    return shape_moi

def get_points(outcome_encoded, shape_moi):
    outcome = outcome_decode[outcome_encoded]
    return shape_points[shape_moi] + outcome_points[outcome]

def execute_part_two():
    
    with open(filename, 'r') as handler:
        nb_lines = len(handler.readlines())
        handler.seek(0)
        
        for nb_line in range(nb_lines):
            line = handler.readline()
            outcome_encoded = line[data.outcome]
            my_shape = get_my_shape(outcome_encoded, line[data.opponent_shape])
            points.append(get_points(outcome_encoded, my_shape))
    
    print("Total des points = ", sum(points))

    
execute_part_two()