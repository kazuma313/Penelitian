from sklearn.model_selection import cross_validate
from sklearn.svm import SVC
from sklearn.metrics import classification_report,confusion_matrix
from sklearn import metrics

from .olahFile import encodingInversTransfom


from .preprocessing import scaling
from .preprocessing import splitData

import pandas as pd
import numpy as np

C = tuple(np.arange(0.1,3.7,0.5)) 
kernel = ('linear', 'poly', 'rbf', 'sigmoid')
max_iter = tuple(np.arange(-1, 1000, 400))
degree = tuple(np.arange(1, 1000, 250))
gamma = ('scale', 'auto')
coef0 = tuple(np.arange(0, 5.1, 1.0))


poly = []
rbf = []
linear = []
sigmoid = []
split_data = []


def prosesLinear(C:tuple, max_iter:tuple, x_train: 'array', y_train: 'array', cv : int):
    for i in C :
        for j in max_iter:
            svm = SVC(
              kernel = 'linear',
                C = i,
                max_iter = j
            )

            results = cross_validate(estimator = svm,
                                          X = x_train,
                                          y = y_train,
                                          cv = cv)

    
            score = float(results['test_score'].mean())

            linear.append([score, i, j])  



def prosesRbf(C:tuple, max_iter:tuple, gamma:tuple, x_train: 'array', y_train: 'array', cv : int):
    for i in C:
        for j in max_iter:
            for k in gamma:
                svm = SVC(
                  kernel = 'rbf',
                    C = i,
                    max_iter = j,
                    gamma = k
                )

                results = cross_validate(estimator=svm,
                                          X=x_train,
                                          y=y_train,
                                          cv=cv)

    
                score = float(results['test_score'].mean())
                
                rbf.append([score, i, j, k])             



def prosesSigmoid(C:tuple, max_iter:tuple, gamma:tuple, coef0:tuple, x_train: 'array', y_train: 'array', cv:int):
    for i in C:
        for j in max_iter:
            for k in gamma:
                for l in coef0:
                    svm = SVC(
                      kernel = 'sigmoid',
                        C = i,
                        max_iter = j,
                        gamma = k,
                        coef0 = l
                    )

                    results = cross_validate(estimator=svm,
                                          X = x_train,
                                          y = y_train,
                                          cv = cv)

    
                    score = float(results['test_score'].mean())

                    sigmoid.append([score, i, j, k, l])    



def prosesPoly(C:tuple, max_iter:tuple, gamma:tuple, coef0:tuple, degree:tuple, x_train: 'array', y_train: 'array', cv:int):
    for i in C:
        for j in max_iter:
            for k in gamma:
                for l in coef0:
                    for m in degree:
                        svm = SVC(
                          kernel = 'sigmoid',
                            C = i,
                            max_iter = j,
                            gamma = k,
                            coef0 = l,
                            degree = m
                        )

                        results = cross_validate(estimator=svm,
                                          X = x_train,
                                          y = y_train,
                                          cv = cv)

    
                        score = float(results['test_score'].mean())

                        poly.append([score, i, j, k, l,m])    


def akurasiTiapSplit(x, y, iterasi):
  for i in range(5):
    temp = []
    dTest = 0.0
    for j in range(iterasi):
        dTest += 0.1

        x_train, x_test, y_train, y_test = splitData(x, y, dTest, 101)


        svm = SVC(
        kernel = 'rbf',
        C = 3.6,
        max_iter = 799,
        gamma = 'scale' 
        ) 
        
        svm.fit(x_train,y_train)
        y_pred = svm.predict(x_test)
        score = metrics.accuracy_score(y_test, y_pred)
        
        temp.append([score, round(dTest, 1)])
    split_data.append(temp)



def prosesKernel(x, y, cv, C:list, max_iter:list, gamma:list, coef0:list, degree:list):
    prosesLinear(C, max_iter, x, y, cv)
    prosesRbf(C, max_iter, gamma, x, y, cv)
    prosesSigmoid(C, max_iter, gamma, coef0, x, y, cv)
    prosesPoly(C, max_iter, gamma, coef0, degree, x, y, cv)
    akurasiTiapSplit(x, y, 5)
  
  

def hasilKlasifikasi(banding1:list, banding2:list)->pd.DataFrame:

    hasil_klasifikasi = classification_report(banding1, banding2,output_dict=True)

    hasil_klasifikasi.pop('macro avg')
    hasil_klasifikasi.pop('weighted avg')
    hasil_klasifikasi['mild'].pop('support')
    hasil_klasifikasi['severe'].pop('support')

    hasil_klasifikasi = pd.DataFrame(hasil_klasifikasi).transpose()
    hasil_klasifikasi.iloc[2,:-1] = np.nan
    
    return hasil_klasifikasi


def prosesTrain(x_train:list, y_train:list)->object:   
  svm = SVC(
    kernel = 'rbf',
    C = 3.6,
    max_iter = 799,
    gamma = 'auto'
  )
  svm.fit(x_train,y_train)
  
  return svm
  

def predictDataTesting(x, y, svm, encode:object):

    y_pred = svm.predict(x)
    score = metrics.accuracy_score(y, y_pred)

    y_testNominal = encodingInversTransfom(encode, y)
    y_predictNominal = encodingInversTransfom(encode, y_pred)

    cnfMatrix = confusion_matrix(y_testNominal, y_predictNominal)

    hasil_klasifikasi = hasilKlasifikasi(y_testNominal, y_predictNominal)
    # y_testNominal = encodingInversTransfom(encodeSeverity,y_test)
    # y_predictNominal = encodingInversTransfom(encodeSeverity, y_pred)

    banding = pd.DataFrame({'y_test': y_testNominal, 'y_pred': y_predictNominal}, columns=['y_test', 'y_pred'])


    return score, cnfMatrix, hasil_klasifikasi, banding, y_pred

def predictNewData(data:'Dataframe', svm:object, encode:object ):
    X_dummy_scaled = scaling(data.iloc[:,:-1])
    y_dummy_scaled = data.iloc[:,-1]

    score_dummy, cnfMatrix_dummy, hasil_klasifikasi_dummy, banding_dummy, y_pred = predictDataTesting(X_dummy_scaled, y_dummy_scaled, svm, encode)

    return score_dummy, cnfMatrix_dummy, hasil_klasifikasi_dummy, banding_dummy 
  
  