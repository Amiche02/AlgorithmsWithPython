"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from math import *

def smallestMultiple0(x, y):
  mul = 0
  n = y
  while mul==0:
    for i in range(x, y+1):
      if n%i == 0:
        if i==y:
          mul = 1
      else:
        n+=1
        break
        
  return n  

def smallestMultiple(x, y):
    primes = {}
    for i in range(x, y+1):
        factors = []
        n = i
        for j in range(2, int(sqrt(i))+1):
            count = 0
            while n % j == 0:
                n //= j
                count += 1
            if count > 0:
                factors.append((j, count))
        if n > 1:
            factors.append((n, 1))
        primes[i] = factors

    lcm_factors = {}
    for factors in primes.values():
        for p, count in factors:
            if p not in lcm_factors or count > lcm_factors[p]:
                lcm_factors[p] = count

    lcm = 1
    for p, count in lcm_factors.items():
        lcm *= p**count

    return lcm


print(smallestMultiple(1, 20))

"""
def maxrepetition(tab):
  max_count = 0
  max_countnum = None
  for i in tab:
    count = 0
    for j in tab:
      if i == j:
        count += 1
    if max_count<count:
      max_count = count
      max_countnum = i
  return max_countnum
"""

def maxrepetition(tab):
    count_dict = {}
    for x in tab:
        if x in count_dict:
            count_dict[x] += 1
        else:
            count_dict[x] = 1
    max_count = 0
    max_countnum = None
    for x, count in count_dict.items():
        if count > max_count:
            max_count = count
            max_countnum = x
    return max_countnum

