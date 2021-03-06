import numpy as np
from numpy import loadtxt, savetxt
import matplotlib.pyplot as plt

data60 = loadtxt("DROPBEAR NI 9260 synthesis.csv", delimiter=',')
data63 = loadtxt("DROPBEAR NI 9263 synthesis.csv", delimiter=',')
acc = loadtxt("X_test.csv", delimiter=',')
t = loadtxt("t_test.csv", delimiter=',')

acc = np.reshape(acc.T, acc.size)
t = np.reshape(t.T, t.size)
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
#%% analysis of single-sample data with 500 us, 200 us, and 80 us.

data500 = loadtxt("signal generation 500 us.csv", delimiter=',')
t500 = np.array([0.0005 *i for i in range(data500.size)])
data200 = loadtxt("signal generation 200 us.csv", delimiter=',')
t200 = np.array([0.0002 *i for i in range(data200.size)])
data80 = loadtxt("signal generation 80 us.csv", delimiter=',')
t80 = np.array([0.00008 *i for i in range(data80.size)])

plt.figure()
plt.plot((t-t[0]),acc)
plt.plot(t80,data80)

plt.figure()
plt.plot(data80)

time_offset500 = 680
plt.figure(figsize=(7,3))
plt.plot((t-t[0])[:500],acc[:500])
plt.plot(t500[0:50],data500[time_offset500:time_offset500 + 50])
plt.xlim((0,.020))
plt.savefig("500 us signal.png", dpi=500)

time_offset200 = 14617
plt.figure(figsize=(7,3))
plt.plot((t-t[0])[:500],acc[:500])
plt.plot(t200[:500],data200[time_offset200:time_offset200 + 500])
plt.xlim((0,.020))
plt.savefig("200 us signal.png", dpi=500)

time_offset80 = 40622
plt.figure(figsize=(7,3))
plt.plot((t-t[0])[:500],acc[:500])
plt.plot(t80[:500],data80[time_offset80:time_offset80 + 500])
plt.xlim((0,.020))
plt.xlabel("time (s)")
plt.ylabel("signal (V)")
plt.tight_layout()
plt.savefig("80 us signal.png", dpi=500)


acc = loadtxt("X_test.csv", delimiter=',')

acc = np.reshape(acc.T, acc.size)
