import numpy as np
"""

A,X = Rock [1]
B,Y = Paper[2]
C,Z = Scissors[3]
win= 6
lose=0
draw=3
"""
data = open('2_input.txt').read()
a = data.split()

opp= a[::2]
play= a[1::2]

score = 0
for j in range(len(play)):
    if opp[j] == 'A':
        if play[j] == 'X':#draw
            score += 1
            score+= 3
        elif play[j] == 'Y':#win
            score += 2
            score += 6
        elif play[j] == 'Z':#lose
            score += 3
            score+= 0
    elif opp[j] =='B':
        if play[j] == 'X':#lose
            score += 1
            score+= 0
        elif play[j] == 'Y':#win
            score += 2
            score += 3
        elif play[j] == 'Z':#lose
            score += 3
            score+= 6
    elif opp[j] =='C':
        if play[j] == 'X':#win
            score += 1
            score+= 6
        elif play[j] == 'Y':#lose
            score += 2
            score += 0
        elif play[j] == 'Z':#draw
            score += 3
            score+= 3

score2=0
for i in range(len(play)):
    if play[i]=='X':
        score2+=0
        if opp[i]=='A':
            score2+=3
        elif opp[i]=='B':
            score2+=1
        elif opp[i]=='C':
            score2+=2
    elif play[i]=='Y':
        score2+=3
        if opp[i]=='A':
            score2+=1
        elif opp[i]=='B':
            score2+=2
        elif opp[i]=='C':
            score2+=3
    elif play[i]=='Z':
        score2+=6
        if opp[i]=='A':
            score2+=2
        elif opp[i]=='B':
            score2+=3
        elif opp[i]=='C':
            score2+=1
print(score2)