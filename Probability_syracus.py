# -*- coding: utf-8 -*-
"""
Created on Fri May 19 10:41:14 2023

@author: steph
"""

import random

def collatz(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n + 1) // 2
        sequence.append(n)
    return sequence

def collatz_probabilistic(n, iterations):
    sequence = [n]
    for _ in range(iterations):
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n + 1) // 2
        sequence.append(n)
    return sequence

def collatz_randomized(n, iterations):
    sequence = [n]
    for _ in range(iterations):
        if n % 2 == 0:
            n = n // 2
        else:
            n = random.randint(1, n)
        sequence.append(n)
    return sequence

# Exemple d'utilisation
print(collatz(6))
print(collatz_probabilistic(6, 100))
print(collatz_randomized(6, 100))
