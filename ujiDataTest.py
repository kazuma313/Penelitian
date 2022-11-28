from prosesTrain import svm, x_test, y_test
from modul.proses import predictDataTesting
from modul.olahFile import saveFileExcel, encodingInversTransfom
import numpy as np
from preprocessing import encodeSeverity


score, cnfMatrix, hasil_klasifikasi, banding, y_pred = predictDataTesting(x_test, y_test, svm, encodeSeverity)
    
unik = np.unique(y_pred)
trans = encodingInversTransfom(encodeSeverity, unik)

keterangan = ""
for i in range(len(unik)):
    keterangan += f"nilai : {unik[i]} --> {trans[i]}. \n"

saveFileExcel(banding,'PerbandinganHasilPrediksi')

