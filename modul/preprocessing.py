from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import SMOTE

def splitData(x:'DataFrame', y:'Series', test_size:float, random_state:int):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=random_state)
    return x_train.to_numpy(), x_test.to_numpy(), y_train.to_numpy(), y_test.to_numpy()

def scaling(data:'DataFrame'):
    columns = data.columns
    data_scaled = StandardScaler().fit(data.to_numpy())
    data = data_scaled.transform(data.to_numpy()) 
    data = pd.DataFrame(data=data, columns=columns)
    return data

def smote(x:'DataFrame', y:'Siries', strategy:str):
    smote = SMOTE(sampling_strategy=strategy)
    x, y = smote.fit_resample(x, y)
    return x, y
    
def featureImportance(x:'DataFrame', y:'Siries', column_name:str):
    model = LogisticRegression()
    model.fit(x, y)
    importance = model.coef_[0]
    data_imporance = pd.DataFrame({column_name:x.columns, 'score':importance}, columns=[column_name, 'score'])
    
    return data_imporance

def ambil_importance(data:'DataFrame asli', importance:'DataFrame score importance', column1: 'nama columns fitur', column2:'nama columns score', jumlah:int):
    jumlah = round(jumlah/2)
    scoreTertinggi = list(importance.nlargest(jumlah, column2)[column1])
    scoreTerendah = list(importance.nsmallest(jumlah, column2)[column1])
    
    atribut_terpilih = pd.concat([data.loc[:, scoreTertinggi], data.loc[:, scoreTerendah]], axis = 1)
    
    return atribut_terpilih
