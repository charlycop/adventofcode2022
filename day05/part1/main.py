from enum import IntEnum

class move(IntEnum):
   qty      = 1
   src_pile = 3
   tgt_pile = 5

target_info = {move.qty:0, move.src_pile:1, move.tgt_pile:2}

filename       = 'adventofcode/day05/inputs.txt'
datas          = []
full_movements = []

full_load = {1:['P', 'F', 'M', 'Q', 'W', 'G', 'R', 'T'], 
             2:['H', 'F', 'R'],
             3:['P', 'Z', 'R', 'V', 'G', 'H', 'S', 'D'],
             4:['Q', 'H', 'P', 'B', 'F', 'W', 'G'],
             5:['P', 'S', 'M', 'J', 'H'],
             6:['M', 'Z', 'T', 'H', 'S', 'R', 'P', 'L'],
             7:['P', 'T', 'H', 'M', 'N', 'L'],
             8:['F', 'D', 'Q', 'R'],
             9:['D', 'S', 'C', 'N', 'L', 'P', 'H']
}


def get_mouvements(datas):
    movments = []
    for ligne in datas:
        if ligne[0] != 'm' : continue
        ligne = ligne.split()
        movments.append([int(ligne[move.qty]), int(ligne[move.src_pile]), int(ligne[move.tgt_pile])])

    return movments

# On lit le fichier
with open(filename, 'r') as handler:
    datas = handler.readlines()

# On récupère les mouvements
full_movements = get_mouvements(datas)

# On fait les mouvements
for mouvement in full_movements:
    for i in range(mouvement[target_info[move.qty]]):
        target = mouvement[target_info[move.tgt_pile]]
        source = mouvement[target_info[move.src_pile]]
        full_load[target].append(full_load[source].pop())

#On récupère les caisse en haut des piles dans une string
caisse_haut_de_pile = ""
for pile in full_load.keys():
    caisse_haut_de_pile += full_load.get(pile)[-1]
    
print("Les caisses en haut des piles sont : ", caisse_haut_de_pile)