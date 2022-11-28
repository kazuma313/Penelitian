from modul.olahFile import readFileExcel
from modul.proses import splitData, prosesTrain

# from panggil_data import df_split, x, y, clean_data
df_split = readFileExcel('data\hasil_split0.xlsx')
x = readFileExcel('data\X.xlsx')
y = readFileExcel('data\y.xlsx')

# test_value = df_split[df_split['Akurasi'] == np.max(df_split['Akurasi'])]['dataTest'].iloc[0]
x_train, x_test, y_train, y_test = splitData(x, y, 0.5, 101)
  

svm = prosesTrain(x_train, y_train)
