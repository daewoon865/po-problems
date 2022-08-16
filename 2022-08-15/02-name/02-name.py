import sys
input = sys.stdin.readlines()
T = int(input[0])
input = input[1:]

def check (word1: str, word2: str) -> bool:
    track = dict()
    for i in word1:
        if track.get(i) is None:
            track[i] = 1
        else:
            track[i] = track[i] + 1
    
    for i in word2:
        if track.get(i) == 1:
            del (track[i])
        elif track.get(i) is not None:
            track[i] = track[i] - 1

    return len(track) == 0

for i in input:
    i.strip()
    couple = i.split(" ")
    couple = [i.lower() for i in couple]

    if check(couple[0], couple[1]) or check(couple[1], couple[0]):
        print ("YES")
    else:
        print("NO")

