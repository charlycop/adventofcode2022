filename = 'inputs.txt'
datas = []
somme = 0

debut_ascii_maj = ord('A')
debut_ascii_min = ord('a')
nb_lettres = (ord('Z')+1) - ord('A')

def get_priority(letter):
    code_chr = ord(letter)
    if code_chr >= debut_ascii_min:
        return code_chr - (debut_ascii_min-1)
    
    return code_chr - (debut_ascii_maj-1) + nb_lettres
 
with open(filename, 'r') as handler:
    datas = handler.readlines()

for liste in datas:
    if liste[-1] == '\n' : liste = liste[:-1]
    first_half  = liste[:int(len(liste)/2)]
    second_half = liste[int(len(liste)/2):]
    
    for c in first_half:
        if second_half.find(c) >= 0 : 
            somme += get_priority(c)
            break
    
print("Somme des priorités = ", somme)
    

