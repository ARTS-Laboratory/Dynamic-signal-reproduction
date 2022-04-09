import numpy as np
from numpy import loadtxt, savetxt
import matplotlib.pyplot as plt

data60 = loadtxt("DROPBEAR NI 9260 synthesis.csv", delimiter=',')
data63 = loadtxt("DROPBEAR NI 9263 synthesis.csv", delimiter=',')
acc = loadtxt("X_test.csv", delimiter=',')

acc = np.reshape(acc.T, acc.size)
# data_length = acc.size

# plt.figure()
# plt.plot(acc)

# plt.figure()
# plt.plot(data60)

# plt.figure()
# plt.plot(data63)
#%% finding time offsets
time_offset60 = 14140
plt.figure(figsize=(7,3))
plt.plot(acc[:500])
plt.plot(data60[time_offset60:time_offset60 + 500])
plt.savefig("9260 synthesis.png", dpi = 400)

time_offset63 = 13688
plt.figure(figsize=(7,3))
plt.plot(acc[:500])
plt.plot(data63[time_offset63:time_offset63 + 500])
plt.savefig("9263 synthesis.png", dpi = 400)

#%% finding RMSE.
from sklearn.metrics import mean_squared_error

rmse60 = mean_squared_error(data60[time_offset60:time_offset60+20000], acc[:20000], squared=False)
# plt.figure()
# plt.plot(acc[:20000])
# plt.plot(data60)
# plt.plot(error60)
data63 = data63[time_offset63:]
rmse63 = mean_squared_error(data63, acc[:data63.size], squared=False)
#%% export to find SNR in MATLAB
savetxt("9260.csv", data60[time_offset60:time_offset60+20000],delimiter=',')
savetxt("9260acc.csv", acc[:20000],delimiter=',')
savetxt("9263.csv", data63, delimiter=',')
savetxt("9263acc.csv", acc[:data63.size], delimiter=',')

