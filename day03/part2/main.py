filename = 'day03/inputs.txt'
datas = []
somme = 0
nb_lettres = ord('Z') - ord('A') + 1
taille_groupe = 3

def get_priority(letter):
    code_chr = ord(letter)
    if code_chr >= ord('a'):
        return code_chr - (ord('a')-1)
    
    return code_chr - (ord('A')-1) + nb_lettres
 
with open(filename, 'r') as handler:
    datas = handler.readlines()

for i in range(0, len(datas), taille_groupe):

    for c in datas[i]:
        if datas[i+1].find(c) >= 0 and datas[i+2].find(c) >= 0: 
            somme += get_priority(c)
            break
    
print("Somme des priorités des groupes de", taille_groupe,"elfes = ", somme)