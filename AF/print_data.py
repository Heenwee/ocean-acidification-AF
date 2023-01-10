from ezodf import opendoc, Sheet
import matplotlib.pyplot as plt

doc = opendoc("Arctic_Frontiers Data.ods")
data = doc.sheets[1]

days = [1, 2, 5, 6, 7]

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

print(f"average thickness 7.7:{data_average(3, 9, 15, 17)}")
print(f"average thickness 7.5:{data_average(3, 9, 18, 20)}")
print(f"average thickness 7.3:{data_average(3, 9, 21, 23)}")
print(f"average thickness 7.1:{data_average(3, 9, 24, 26)}")

print(f"average mass 7.7: {data_average(15, 21, 15, 17)}")
print(f"average mass 7.5: {data_average(15, 21, 18, 20)}")
print(f"average mass 7.3: {data_average(15, 21, 21, 23)}")
print(f"average mass 7.1: {data_average(15, 21, 24, 26)}")