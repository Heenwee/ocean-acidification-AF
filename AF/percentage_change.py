from ezodf import opendoc, Sheet
import matplotlib.pyplot as plt

doc = opendoc("Arctic_Frontiers Data.ods")
data = doc.sheets[1]

days = [1, 2, 5, 6, 7]

def data_series(startrow, endrow, startcol, endcol):
    fin_array = []
    for i in range(endcol-startcol+1):
        arr = []
        for j in range(endrow-startrow+1):
            cell = data[startrow+j, startcol+i]
            if cell.value_type != None:
                arr.append(cell.value*100)
        fin_array.append(arr)
    return fin_array

plt.subplot(121)
plt.title("Thickness (%)")
plt.grid()
for i in range(3):
    plt.plot(days, data_series(3, 9, 15, 17)[i], label='7.7', color='C0')
    plt.plot(days, data_series(3, 9, 18, 20)[i], label='7.5', color='C1')
    plt.plot(days, data_series(3, 9, 21, 23)[i], label='7.3', color='C2')
    plt.plot(days, data_series(3, 9, 24, 26)[i], label='7.1', color='C3')
plt.ylim(75, 110)
plt.xlabel("Days")
plt.ylabel("Change")
plt.legend(["7.7", "7.5", "7.3", "7.1"])

plt.subplot(122)
plt.title("Mass (%)")
plt.grid()
for i in range(3):
    plt.plot(days, data_series(15, 21, 15, 17)[i], label='7.7', color='C0')
    plt.plot(days, data_series(15, 21, 18, 20)[i], label='7.5', color='C1')
    plt.plot(days, data_series(15, 21, 21, 23)[i], label='7.3', color='C2')
    plt.plot(days, data_series(15, 21, 24, 26)[i], label='7.1', color='C3')
plt.ylim(75, 110)
plt.xlabel("Days")
plt.ylabel("Change")
plt.legend(["7.7", "7.5", "7.3", "7.1"])

plt.show()