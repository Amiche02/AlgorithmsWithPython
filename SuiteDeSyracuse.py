import numpy as np


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



n = 1
while n == 1:
  n = input("Entrez le nombre que vous voulez : ")
  try:
    n = int(n)
  except:
    print("Entrez un nombre valide.\n")
  else:
    list_ = syracuse(n)

array = np.array(list_)
print(array)
