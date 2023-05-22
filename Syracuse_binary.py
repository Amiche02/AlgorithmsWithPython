# -*- coding: utf-8 -*-
"""
Created on Fri May 19 09:24:34 2023

@author: steph
"""

def syracuse_binary(n):
    sequence = []
    while n != 1:
        sequence.append(bin(n)[2:])
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n + 1) // 2
    sequence.append(bin(n)[2:])
    return sequence

# Exemple d'utilisation
start_number = 7
binary_sequence = syracuse_binary(start_number)

for i, num in enumerate(binary_sequence):
    print(' ' * (len(binary_sequence) - i), num)
