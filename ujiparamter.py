from modul.olahFile import readFileExcel, saveFileExcel
from modul.proses import prosesKernel, rbf, poly, linear, sigmoid, split_data
import pandas as pd


x = readFileExcel('data\X.xlsx')
y = readFileExcel('data\y.xlsx')

prosesKernel(x, y, 5)

df_poly = pd.DataFrame(poly, columns = "Akurasi C Max_itter Gamma Coef0 Degree".split())
df_rbf = pd.DataFrame(rbf, columns="Akurasi C Max_itter Gamma".split())
df_linear = pd.DataFrame(linear, columns="Akurasi C Max_itter".split())
df_sigmoid = pd.DataFrame(sigmoid, columns="Akurasi C Max_itter Gamma Coef0".split())

# test_value = df_split[df_split['Akurasi'] == np.max(df_split['Akurasi'])]['dataTest'].iloc[0]

saveFileExcel(df_linear,'hasil_Linear')
saveFileExcel(df_rbf,'hasil_RBF')
saveFileExcel(df_sigmoid,'hasil_sigmoid')
saveFileExcel(df_poly,'hasil_poly')

print(split_data)
print(len(split_data))
print(len(split_data[0]))
print(len(split_data[0][0]))
for i in range(5):
    df_split = pd.DataFrame(split_data[i], columns="Akurasi dataTest".split())
    saveFileExcel(df_split,f'hasil_split{i}')

rata2_akurasi= []

for i in range(len(split_data[0])):
    temp = 0.0
    for j in range(len(split_data)):
        print(split_data[j][i][0])
        temp += split_data[j][i][0]
    print("jumlah :", temp) 
    temp = temp/len(split_data)
    print("rata-rata", temp)
    rata2_akurasi.append([temp, len(split_data[0])])
    
df_rata2_akurasi = pd.DataFrame(rata2_akurasi, columns = "Akurasi datatest".split())
saveFileExcel(df_rata2_akurasi, "hasil_rata2_split")