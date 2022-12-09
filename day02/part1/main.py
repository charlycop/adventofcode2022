from enum import IntEnum

filename = 'day02/inputs.txt'
shape_points = {"X" : 1, "Y" : 2, "Z" : 3}
outcome_points = {"won" : 6, "draw" : 3, "lost" : 0}
shape_equiv = {"X" : "A", "Y" : "B", "Z" : "C"}
points = []

class Player(IntEnum):
   moi = 2
   opponent = 0

def get_outcome (shape_opponent, shape_moi):
    outcome = "won"
    
    if  (shape_opponent == shape_equiv[shape_moi]):
        outcome = "draw"
    elif(shape_opponent == "A" and shape_moi == "Z") or (shape_opponent == "B" and shape_moi == "X") or (shape_opponent == "C" and shape_moi == "Y"):
        outcome = "lost"
    
    return outcome

def get_points(outcome, shape_moi):
    return shape_points[shape_moi] + outcome_points[outcome]

def execute_part_one():
    
    with open(filename, 'r') as handler:
        nb_lines = len(handler.readlines())
        handler.seek(0)
        
        for nb_line in range(nb_lines):
            line = handler.readline()
            outcome = get_outcome(line[Player.opponent], line[Player.moi])
            points.append(get_points(outcome, line[Player.moi]))
    
    print("Total des points = ", sum(points))

    
execute_part_one()
