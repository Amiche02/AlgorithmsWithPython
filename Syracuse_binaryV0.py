# -*- coding: utf-8 -*-
"""
Created on Fri May 19 09:49:58 2023

@author: steph
"""

#Binary approach

def binarynumber(uo):
    n = int(uo)
    mod = []
    bin_ = 0
    while n>1:
        mod.append(n%2)
        n //= 2
    mod.append(n)
    for i in range(1, len(mod)+1):
        bin_ = bin_*10 + mod[-i]
    return str(bin_)


def dropRightZero(n):
    n = str(n)
    i = -1
    while int(n[i])==0:
        n = n[:len(n)-1]
        i-=1
    return n

def binaryAddition(n, m):
    n, m = str(n), str(m)
    diff = abs(len(m)-len(n))
    if len(n) < len(m):
        n = diff*"0" + n
    else:
        m = diff*"0" + m
    
    carry = 0
    result = ''
    for i in range(len(n)-1, -1, -1):
        sum_ = int(n[i]) + int(m[i]) + carry
        if sum_ == 0:
            result = '0' + result
            carry = 0
        elif sum_ == 1:
            result = '1' + result 
            carry = 0
        elif sum_ == 2:
            result = '0' + result 
            carry = 1
        else:
            result = '1' + result 
            carry = 1
            
    if carry == 1:
        result = '1' + result
        
        
    return result

"""
def binary_addition(n, m):
    n, m = str(n), str(m)
    # Convertir les nombres binaires en listes d'entiers
    n = [int(x) for x in n]
    m = [int(x) for x in m]

    # Ajouter des zéros à gauche pour égaliser la longueur des listes
    diff = abs(len(n) - len(m))
    if len(n) < len(m):
        n = [0]*diff + n
    else:
        m = [0]*diff + m

    # Addition bit à bit
    reserved = 0
    result = []
    for i in range(len(n)-1, -1, -1):
        sum_ = n[i] + m[i] + reserved
        if sum_ == 0:
            result.insert(0, 0)
            reserved = 0
        elif sum_ == 1:
            result.insert(0, 1)
            reserved = 0
        elif sum_ == 2:
            result.insert(0, 0)
            reserved = 1
        else:  # somme == 3
            result.insert(0, 1)
            reserved = 1

    if reserved == 1:
        result.insert(0, 1)

    # Convertir la liste d'entiers en chaîne de caractères binaire
    binary_result = ''.join([str(x) for x in result])

    return binary_result
"""


def syracuse_binary(n):
    sequence = []
    while n != 1:
        sequence.append(binarynumber(n))
        if int(n) % 2 == 0:
            n = int(n) // 2
        else:
            n =  binaryAddition (n, (3 * int(n) + 1) // 2)
        n = dropRightZero(n)
    sequence.append(binarynumber(n))
    return sequence

print(syracuse_binary(7))