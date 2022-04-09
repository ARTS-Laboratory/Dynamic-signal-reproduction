import numpy as np
from numpy import loadtxt
import matplotlib.pyplot as plt

data60 = loadtxt("DROPBEAR NI 9260 synthesis.csv", delimiter=',')
data63 = loadtxt("DROPBEAR NI 9263 synthesis.csv", delimiter=',')
acc = loadtxt("X_test.csv", delimiter=',')



acc = np.reshape(acc.T, acc.size)
data_length = acc.size

plt.figure()
plt.plot(acc)

plt.figure()
plt.plot(data60)

plt.figure()
plt.plot(data63)

plt.figure()
plt.plot(acc - data60[:data_length])


magic_number = 14700
plt.figure()
plt.plot(acc[:250])
plt.plot(data63[magic_number:magic_number + 250])