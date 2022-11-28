from preprocessing import encodeSeverity
import numpy as np
from modul.olahFile import readFileExcel, encodingTransform

perbandingan = readFileExcel('data\PerbandinganHasilPrediksi.xlsx')
pred_test = {
    'prediksi' : encodingTransform(encodeSeverity, perbandingan, 'y_pred')['y_pred'].tolist(),
    'y_test' : encodingTransform(encodeSeverity, perbandingan, 'y_test')['y_test'].tolist(),
    'index' : np.arange(0,perbandingan.shape[0]).tolist()
}
