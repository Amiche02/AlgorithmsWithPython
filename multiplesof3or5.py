"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def multipleOf3and5(number):
  sum = 0
  for i in range(number):
    if i%3==0 or i%5==0:
      sum += i
  return sum


n = int(input("Enter the max number : "))
sum = multipleOf3and5(n)

print(f"The sum of all multiples of 3 or 5 below {n} is {sum}")