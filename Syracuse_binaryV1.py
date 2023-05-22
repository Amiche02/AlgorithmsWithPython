# -*- coding: utf-8 -*-
"""
Created on Fri May 19 09:49:20 2023

@author: steph
"""

def binarynumber(n):
    mod = []
    bin_ = 0
    while n > 1:
        mod.append(n % 2)
        n //= 2
    mod.append(n)
    for i in range(1, len(mod)+1):
        bin_ = bin_*10 + mod[-i]
    return str(bin_)


def dropRightZero(n):
    n = str(n)
    i = -1
    while int(n[i]) == 0:
        n = n[:len(n)-1]
        i -= 1
    return n


def binary_addition(n, m):
    n, m = str(n), str(m)
    
    n = [int(x) for x in n]
    m = [int(x) for x in m]

    diff = abs(len(n) - len(m))
    if len(n) < len(m):
        n = [0]*diff + n
    else:
        m = [0]*diff + m

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

    
    binary_result = ''.join([str(x) for x in result])

    return binary_result


def syracuse_binary(n):
    sequence = []
    while n != 1:
        sequence.append(binarynumber(n))
        if n % 2 == 0:
            n = n // 2
        else:
            n = binary_addition(n, (3 * n + 1) // 2)
        n = dropRightZero(n)
    sequence.append(binarynumber(n))
    return sequence

print(syracuse_binary(7))
