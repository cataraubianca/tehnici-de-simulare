import numpy as np
import matplotlib.pyplot as plt

nr_persoane = 35
aceeasi_zi = 0
nr_experimente = 0
lista_probabilitati = []

np.random.seed(10)

for iteratii in range(0,1000):

  array_zile = np.random.randint(1,366, nr_persoane)

  if len(np.unique(array_zile)) != len(array_zile):
    aceeasi_zi+=1

  nr_experimente += 1

  lista_probabilitati.append(aceeasi_zi/nr_experimente)

plt.plot(lista_probabilitati)
plt.title("Dupa 1000 de iteratii probabilitatea este de " + str(lista_probabilitati[999]))
plt.show()
