from ezodf import opendoc
import matplotlib.pyplot as plt
import numpy as np
from scipy import optimize

doc = opendoc("Arctic_Frontiers Data.ods")
data = doc.sheets[1]

colours = ['C0', 'C1', 'C2', 'C3']

def data_average(startrow, endrow, startcol, endcol):
    data_array = []
    fin_array = []
    for i in range(endcol-startcol+1):
        arr = []
        for j in range(endrow-startrow+1):
            cell = data[startrow+j, startcol+i]
            if cell.value_type != None:
                arr.append(cell.value*100)
        data_array.append(arr)
    for i in range(len(data_array[0])):
        s = 0
        for j in range(len(data_array)):
            s += data_array[j][i]
        fin_array.append(s/len(data_array))
    return fin_array

X = np.array([1, 2, 5, 6, 7])
Y = []
Y.append(data_average(3, 9, 15, 17))
Y.append(data_average(3, 9, 18, 20))
Y.append(data_average(3, 9, 21, 23))
Y.append(data_average(3, 9, 24, 26))
Y.append(data_average(15, 21, 15, 17))
Y.append(data_average(15, 21, 18, 20))
Y.append(data_average(15, 21, 21, 23))
Y.append(data_average(15, 21, 24, 26))

for i in range(4):
    x_mean = np.mean(X)
    y_mean = np.mean(Y[i])

    n = int(len(Y)/2)

    numer = 0
    denom = 0
    for j in range(n):
        numer += (X[j]-x_mean)*(Y[i][j]-y_mean)
        denom += (X[j]-x_mean)**2
    a = numer/denom
    b = y_mean - (a*x_mean)

    y = a*X+b
    
    plt.subplot(121)
    plt.plot(X, y, label=f"{7.7-i*0.2}, df = {'%.2f'%(y[1]-y[0])}", color=f"C{i}")
    plt.scatter(X, Y[i], color=f"C{i}")

plt.legend()
plt.title("Thickness trend (%)")

plt.xlabel("Days")
plt.ylabel("Change")

plt.ylim(96, 102)

for i in range(4):
    x_mean = np.mean(X)
    y_mean = np.mean(Y[i+4])

    n = int(len(Y)/2)

    numer = 0
    denom = 0
    for j in range(n):
        numer += (X[j]-x_mean)*(Y[i+4][j]-y_mean)
        denom += (X[j]-x_mean)**2
    a = numer/denom
    b = y_mean - (a*x_mean)

    y = a*X+b

    plt.subplot(122)
    plt.plot(X, y, label=f"{7.7-i*0.2}, df = {'%.2f'%(y[1]-y[0])}", color=f"C{i}")
    plt.scatter(X, Y[i+4], color=f"C{i}")

plt.legend()
plt.title("Mass trend (%)")

plt.xlabel("Days")
plt.ylabel("Change")

plt.ylim(96, 102)

plt.show()