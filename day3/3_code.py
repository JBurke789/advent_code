import numpy as np
import textwrap

data = open('day3/3_input.txt').read().split()

#set up items and corresponding points to have same index
abc= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
points = list(range(1,len(abc)+1))

######Part 1####
score=0
for i in data:
    a = textwrap.wrap(i,int(0.5*len(i))) # split each bag in half
    common_character = ''.join(set(a[0]).intersection(a[1]))#find common character
    index = np.where(np.array(abc) == common_character)#find index of common charcter
    points_per_bag = points[int(index[0])]#find points per bag from index of common item
    score+=points_per_bag#adds points from each bag
print(score)

####Part 2####
#split into groups of three
groups=[]
for i in range(0,len(data),3):
    groups.append(data[i:i+3])

sum=0
for i in groups:#same as above but for groups instead of bags
    common = ''.join(set(i[0]).intersection(i[1]).intersection(i[2]))
    index = np.where(np.array(abc) == common)
    points_per_group = points[int(index[0])]
    sum += points_per_group
print(sum)