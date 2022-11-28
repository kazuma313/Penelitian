import pandas as pd
from sklearn import preprocessing

def readFileCsv(path:str)->'DataFrame':
    data = pd.read_csv(fr'{path}',delimiter=',',engine='python',encoding='windows_1258')
    return data

def readFileExcel(path:str)->'DataFrame':
    data = pd.read_excel(fr'{path}')
    if data.columns[0] == 'Unnamed: 0':
        data = dropColumns(data, ['Unnamed: 0'])
    return data

def saveFileExcel(data:'DataFrame',name:str):
    # if data.columns[0] == 'Unnamed: 0':
    #     data = dropColumns(data, ['Unnamed: 0'])
    data.to_excel("data/"+name+".xlsx")
    
def saveFileCsv(data:'DataFrame',name:str):
    data.to_csv("data/"+name+".csv")

def changeColumns(data:'DataFrame',columns:list):
    data.columns = columns.copy()
    return data

def dropColumns(data:'DataFrame', cloumns:list):
    data.drop(cloumns, axis=1, inplace=True)
    return data

def encodeData(data:'DataFrame', columns:str):
    encoder = preprocessing.LabelEncoder()
    encoder.fit(data[columns])

    return encoder

def encodingTransform(encoder:'Encoder', data:'DataFrame', columns:str):
    trans_col = encoder.transform(data[columns])
    data[columns] = trans_col  
    
    return data

def encodingInversTransfom(encoder:'Encoder', data:'Array'):
    invers_Trans = encoder.inverse_transform(data)
    
    return invers_Trans

def independent_dependent(data:'DataFrame',y_label:str)->'data X dan data Y':
    y = data.pop(y_label)
    x = data
    return x,y