# declare constants 
MARKER_LENGTH = 14

filename = 'day06/inputs.txt'
datas = []

with open(filename, 'r') as handler:
    datas = handler.readlines()
    datas = datas[0]

marker_found = True

for i in range(MARKER_LENGTH, len(datas)):
    message_marker = datas[i-MARKER_LENGTH:i]
    
    for letter in message_marker:
        if message_marker.count(letter) > 1 : 
            marker_found = False
            break
    
    if marker_found : break
    else : marker_found = True

if marker_found:
    print("First marker after character : ", i)
else:
    print("No Marker Found !")

