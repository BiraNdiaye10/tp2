##### question 1
resultat = []
for i in range(2000, 3000):
    if i%7 == 0  and i%5 ==0:
        resultat.append(i)
print(resultat)

#### question 2
nbr = int(input('Entrez un nombre : '))
fact = 1
for i in range(1, nbr+1):
  fact = fact * i
print (nbr,'! = ',fact)

### question 3
nbr = int(input('Entrez un nombre : '))
a=0
dico={}
for i in range(1,nbr) :
    a=i*i;
    dico[i]=a;
print (dico)

#### question 5
import numpy as np

tab = np.array([[1,2,3]])
tab1=tab.tolist()
print(tab1)


#### question 6
import numpy as np
x = [0, 1,2]
y = [2, 1, 0]
X = np.stack((x, y))
A=np.cov(X)
print(A)

### question 7
