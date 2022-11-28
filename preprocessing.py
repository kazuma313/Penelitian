import pandas as pd
from modul.olahFile import readFileCsv, changeColumns, dropColumns, encodeData, independent_dependent, encodingTransform, saveFileExcel

from modul.preprocessing import scaling, smote, featureImportance, ambil_importance


filePath = r'F:\python\penelitian\covid-90data-main\90_neut_all.csv'
columnsName = pd.read_csv(r'F:\python\penelitian\covid-90data-main\train_data_finally.csv').columns.to_list()
dropAtribut = ['Blood_system_diseases','Chinese_medicine', 'Anti_infective_treatment', 'Oxygen_therapy', 'ICU', 'FG_infection', 'antiviral_therapy',  'Oxygen_therapy', 'onset_time', 'Actual_days', 'other']

raw_data = readFileCsv(filePath)


clean_data = raw_data.copy()
clean_data = changeColumns(clean_data,columnsName)
clean_data = dropColumns(clean_data,['Unnamed: 0'])

encodeGender = encodeData(clean_data, 'Gender')
encodeSeverity = encodeData(clean_data, 'Severity')

clean_data = encodingTransform(encodeGender, clean_data,'Gender')
clean_data = encodingTransform(encodeSeverity, clean_data,'Severity')
clean_data = dropColumns(clean_data, dropAtribut)

# saveFileExcel(independent_dependent(clean_data, 'Severity'),'data_cleaned')
x_clean, y_clean = independent_dependent(clean_data, 'Severity')

x_scaled = scaling(x_clean)
# scaled_data = x_raw.copy() 

x_smote, y_smote = smote(x_scaled, y_clean, 'minority')
# smoted_data = x.copy()

importance = featureImportance(x_smote, y_smote, 'Gejala')
x_import = ambil_importance(x_smote, importance, 'Gejala','score', 20)


saveFileExcel(raw_data,'data_mentah')
saveFileExcel(pd.concat([x_clean, y_clean],axis=1), 'CleanedData')
saveFileExcel(pd.concat([x_smote,y_smote], axis=1), 'Smoted_data')
saveFileExcel(pd.concat([x_scaled, y_clean], axis=1), 'Scaled_data')
saveFileExcel(importance, 'FeatureImportance')
saveFileExcel(pd.concat([ambil_importance(x_clean, importance, 'Gejala', 'score', 20), y_clean], axis=1), 'CleanedData_Terpilih')
saveFileExcel(x_import, 'X')
saveFileExcel(y_smote, 'y')

saveFileExcel(importance.nlargest(10, 'score'),'importance_tertinggi')
saveFileExcel(importance.nsmallest(10, 'score'),'importance_terendah')