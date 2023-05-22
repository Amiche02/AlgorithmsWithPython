"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def inverse(number):
  n = number
  inv = 0
  while n != 0:
    inv = inv*10 + (n%10)
    n //= 10

  return inv

def ispalindrom(number):
  if number == inverse(number):
    return True
  return False


def largestPalindromProduct():
  pal = []
  for i in range(100, 1000):
    for j in range(100, 1000):
      product = i*j
      if ispalindrom(product):
        pal.append((i, j, product))
  result = max(pal, key=lambda x: x[2])
  return result


number = int(input("Enter  integer number : "))

print(f"number = {number} \nInverse = {inverse(number)} \nPalindrom = {ispalindrom(number)}")

print(f"\nLargest Palindrom Product = {largestPalindromProduct()}")