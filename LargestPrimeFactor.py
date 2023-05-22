"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from math import *
import time


#Best practice
starttime = time.time()
def largestprimefactor(number):
    i = 2
    while i <= sqrt(number):
        if number % i == 0:
            number //= i
        else:
            i += 1
    return number

endtime = time.time()
time_ = endtime - starttime
print(f"\nFirst Method : {largestprimefactor(600851475143)}   ------> time : {time_} second")

#Another method
starttime = time.time()
def ifprimenumber(number):
  if number != 2:
    for i in range(2, int(sqrt(number))):
      if number%i==0:
        return False
  return True

def largestprimefactor1(number):
  tab = []
  for i in range(2, int(sqrt(number))):
    if ifprimenumber(i):
      if number%i==0:
        tab.append(i)
  return max(tab)

endtime = time.time()
time_ = endtime - starttime
print(f"\n\nSecond Method : {largestprimefactor1(600851475143)}   ------> time : {time_} second")