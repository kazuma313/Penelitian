# from crypt import methods
from cProfile import label
from flask import Flask, render_template, url_for, request, jsonify
from itsdangerous import json
from werkzeug.utils import secure_filename

from modul.olahFile import readFileExcel
from modul.proses import predictNewData
from prosesTrain import svm
from preprocessing import encodeSeverity, importance, independent_dependent, ambil_importance
import pandas as pd

from ujiDataTest import keterangan, cnfMatrix, score, banding, hasil_klasifikasi

import os

from json_hasil import pred_test
from json_featureImportance import featureImportance_dictionary
from json_kernel import data_dictionary

app = Flask(__name__)


# @app.route('/', methods = ["GET", "POST"])
# @app.route('/<nama>')
# def proses(nama="Kurnia Zulda Matondang"):
#     pesan = ""
#     nama_table = "Data cleaning"
#     if request.method == "POST":
#         f = request.files['file']
#         f.save(f"data/{secure_filename(f.filename)}")
#         pesan = "file berhasil disimpan"
    
#         # pesan = "file gagal disimpan"

#     return render_template('content.html', nama_table=nama_table , pesan=pesan ,nama=nama)

@app.route('/')
def proses(nama="Kurnia Zulda Matondang"):
    pesan = ""
    return render_template('content.html', nama=nama)

# raw data
@app.route('/raw_data')
def rawData():
    nama_hal = "raw data"
    raw_data = readFileExcel('data\data_mentah.xlsx')
    return render_template('raw_data.html', nama_hal=nama_hal, tables = [raw_data.to_html(index=False, table_id="datatablesSimple")], lebel=label)

# cleaning
@app.route("/cleaning")
def cleaning():
    nama_hal = "data cleaning"
    clean_data = readFileExcel('data\CleanedData.xlsx')
    return render_template('cleaning.html', nama_hal=nama_hal, tables = [clean_data.to_html(index=False, table_id="datatablesSimple")], label=label)

# scaling
@app.route("/scaling")
def scaling():
    nama_hal = "data scaling"
    scaled_data = readFileExcel('data\Scaled_data.xlsx')
    return render_template('scaling.html', nama_hal = nama_hal, tables = [scaled_data.to_html(index=False, table_id="datatablesSimple")], label=label)

# smote
@app.route("/smote")
def smote_():
    nama_hal = "data smote"
    smoted_data = readFileExcel('data\Smoted_data.xlsx')
    return render_template('smote.html', nama_hal = nama_hal, tables = [smoted_data.to_html(index=False, table_id="datatablesSimple")], label = label)

# feature importance
@app.route("/featureImportance")
def featureImportance():
    nama_hal = "Feature Importance"
    importance = readFileExcel('data\FeatureImportance.xlsx')
    return render_template('featureImportance.html', nama_hal = nama_hal)

# hub parameter
@app.route("/hub_parameter")
def HubParameter():
    nama_hal = "Hubungan Parameter"
    return render_template('HubParameter.html', nama_hal = nama_hal)

@app.route("/prediksiKlasifikasi")
def prediksiKlasifikasi():
    nama_hal = "Prediksi Klasifikasi"
    return render_template('prediksiKlasifikasi.html', nama_hal = nama_hal, keterangan = keterangan, akurasi=score,tables = [banding.to_html(index=False, table_id = "datatablesSimple")], label = label)

@app.route("/performa")
def performa():
    nama_hal = "Performa"
    return render_template('performa.html', nama_hal = nama_hal, conf = cnfMatrix, akurasi=score, tables = [hasil_klasifikasi.to_html(table_id = "datatablesSimple")], label = label)


@app.route('/Uji_coba', methods = ["GET", "POST"])
def ujiCoba():
    nama_hal = "Uji Coba"
    cek = request.method == "POST"
    if cek:
        f = request.files['file']
        f.save(f"data/{secure_filename(f.filename)}")
        data_dummy = readFileExcel(f'data/{f.filename}')
    
        X_dummy, y_dummy = independent_dependent(data_dummy, 'Severity')
        
        X_dummy = ambil_importance(X_dummy, importance, 'Gejala', 'score', 20)
        
        dummy = pd.concat([X_dummy, y_dummy], axis=1)
        
        score_dmy, cnf_dmy, hasil_dmy, banding_dummy = predictNewData(dummy, svm, encodeSeverity)
        
        return render_template('Uji_coba.html',request = cek, nama_hal = nama_hal, keterangan = keterangan, akurasi=score_dmy,tables = [banding_dummy.to_html(index=False, table_id = "datatablesSimple")], label = label)

    else:
        return render_template('Uji_coba.html', request = cek, nama_hal = nama_hal)
    
# membuat api
@app.route('/api/SVM/')
def api_SVM():
    return jsonify(data_dictionary)

@app.route('/api/featureImportance/')
def api_featureImportance():
    return jsonify(featureImportance_dictionary)

@app.route('/api/prediksi/')
def api_prediksi():
    return jsonify(pred_test)


with app.test_request_context():
    print(url_for('proses'))
    # print(url_for('uploader'))
    # print(url_for('login',next='/'))


print(os.path.abspath("tempaltes"))
if __name__ == '__main__':
    app.secret_key='ItIsSecret'
    app._static_folder = os.path.abspath("static/")    
    app.debug = True
    app.env="development"
    app.run()