# -*- coding: utf-8 -*-
#import numpy as np
#import matplotlib.pyplot as plt

#Approche de la conjecture
def syracuse(uo):
  list_ = [uo]
  while True:
    if list_.count(1) != 3:
      if uo%2==0:
        uo //= 2
      else:
        uo = uo*3 + 1
      list_.append(uo)
    else:
      return list_


def compressedSyracuse(uo):
  list_ = [uo]
  while True:
    if list_.count(1) != 3:
      if uo%2==0:
        uo //= 2
      else:
        uo = (uo*3 + 1)//2
      list_.append(uo)
    else:
      return list_

#Approche inverse
def inverseSyracus(uo=1, n=10):  
    current_number = [uo] 
    sequence = [current_number]
    
    for i in range(n):
        current_number = sequence[i]
        for j in current_number:
            if j % 6 in [0, 1, 2, 3, 5]:
                sequence.append([2*j])
            elif j % 6 == 4:  
                sequence.append([(j-1)//3,2*j])
                       
    return sequence

def inverseSyracus1(uo = 1, n=10):
    sequence = [uo]
    for i in range(n):
        if sequence[i] % 6 in [0, 1, 2, 3, 5]:
            un = [sequence[i]*2]
        elif sequence[i] % 6 == 4:
            un = [2*sequence[i],(sequence[i]-1)//3]
        for j in un:
            if j not in sequence:
                sequence.append(j)
    return sequence


def inverseSyracus2(uo=1, n=10):  
    current_number = [uo] 
    sequence = [current_number]
    
    for i in range(n):
        current_number = sequence[i]
        for j in current_number:
            if j % 6 in [0, 1, 2, 3, 5]:
                un = [2*j]
                if un not in sequence:
                    sequence.append(un)
            elif j % 6 == 4: 
                un = [(j-1)//3,2*j]
                if un not in sequence:
                    sequence.append(un)
                       
    return sequence



"""
n = 1
while n == 1:
  n = input("Entrez le nombre que vous voulez : ")
  try:
    n = int(n)
  except:
    print("Entrez un nombre valide.\n")
  else:
    list_ = inverseSyracus(n)
"""
#list_ = inverseSyracus2(1, 20)
#array = np.array(list_)
#print(list_)
"""
x = np.arange(len(array))

plt.figure()
plt.plot(x, array)
"""

