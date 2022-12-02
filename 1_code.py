import numpy as np

file = '1_input.txt'

data = open(file).read()

#splits food per elf
elf = data.split('\n\n')

cals=[]
for i in elf:
    cal_elf = sum([int(j) for j in i.split()])
    cals.append(cal_elf)

print('max cals: ' + str(max(cals)))

#reorder cals max to min
cals_sorted = sorted(cals,key=int, reverse=True)
top3_comb = cals_sorted[0]+cals_sorted[1]+cals_sorted[2]
print('three combined: ' + str(top3_comb))
