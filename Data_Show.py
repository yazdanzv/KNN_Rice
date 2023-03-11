import numpy as np

from Normalize import *
from texttable import Texttable
N = 10

data, data_tr = read()
print(f"Showing First {N} Data")
t1 = Texttable()
temp1 = [['Row Number', 'Data']]
for i in range(N):
    temp1.append([i+1, data[i]])
t1.add_rows(temp1)
print(t1.draw())
print("*************************************************************")
print("Number of Rows and Columns")
t2 = Texttable()
temp2 = [['Number of Rows', 'Number of Columns'], [len(data), len(data_tr)]]
t2.add_rows(temp2)
print(t2.draw())
print("*************************************************************")
print("Max And Min Element Per Feature")
temp = [['Feature', 'Max', 'Min']]
for i in range(len(data_tr)):
    temp.append([f"Number {i+1}", np.max(data_tr[i]), np.min(data_tr[i])])
t = Texttable()
t.add_rows(temp)
print(t.draw())


