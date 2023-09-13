import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
import matplotlib.pyplot as plt
 
#CSVファイルをUTF-8形式で読み込む
data = pd.read_csv('20230912.csv',encoding = 'sjis')
#dataを出力
print(data)

print(data["time"][0])
print(data["temp"][0])
	

first_column_data = data["time"]
second_column_data =data["temp"]

#plt.xlabel(input_csv.keys()[0])
#plt.ylabel(input_csv.keys()[1])

fig = plt.figure()
plt.plot(first_column_data, second_column_data, linestyle='solid', marker='o')
#plt.show()
fig.savefig("img.png")
