from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.utils  import secure_filename
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import time 
import numpy as np
# from sklearn.externals import joblib

# import sklearn.external.joblib as extjoblib
import joblib




# Import sklearn modelling tools 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier



app = Flask(__name__)

test_data = [[150, 1, 0, 1587, 6707, 0, 0, 0, 1, 0, 1, 3, 0, 0, 1, 0, 0, 0, 1, 1, 0.0, 0.0, 1.0, 0.0, 0.0, 1, 1, 0.00, 1.00, 0.00]]


Spc = joblib.load('pca3.joblib')

model = joblib.load('random_forestMain.joblib')





@app.route('/')
def index():    
    return render_template('index.html')


@app.route('/input')
def input():    
    return render_template('input.html')


@app.route('/predict', methods=['POST'])
def process():
    data1 = int(request.form['input1'])
    data2 = int(request.form['input2'])
    data3 = int(request.form['input3'])
    data4 = int(request.form['input4'])
    data5 = int(request.form['input5'])
    data6 = int(request.form['input6'])
    data7 = int(request.form['input7'])
    data8 = int(request.form['input8'])
    data9 = int(request.form['input9'])
    data10 = int(request.form['input10'])
    data11 = int(request.form['input11'])
    data12 = int(request.form['input12'])
    data13 = int(request.form['input13'])
    data14 = int(request.form['input14'])
    data15 = int(request.form['input15'])
    data16 = int(request.form['input16'])
    data17 = int(request.form['input17'])
    data18 = int(request.form['input18'])
    data19 = int(request.form['input19'])
    data20 = int(request.form['input20'])
    data21 = int(request.form['input21'])
    data22 = int(request.form['input22'])
    data23 = int(request.form['input23'])
    data24 = int(request.form['input24'])
    data25 = int(request.form['input25'])
    data26 = int(request.form['input26'])
    data27 = int(request.form['input27'])
    data28 = int(request.form['input28'])
    data29 = int(request.form['input29'])
    data30 = int(request.form['input30'])

    data=[[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16,data17,data18,data19,data20,data21,data22,data23,data24,data25,data26,data27,data28,data29,data30]]

    
  
    X_test_pca = Spc.transform(data)
    result = model.predict(X_test_pca)
    print(result)

    if result==[0]:
        r="No Intrution Detected"
    if result==[1]:
        r="Intrution Detected - Dos"
    if result==[2]:
        r="Intrution Detected - Probe"
    if result==[3]:
        r="Intrution Detected - R2L"
    if result==[4]:
        r="Intrution Detected - U2R"

    
    return "<script>alert('"+r+"');window.location.href = '/input';</script>"


# @app.route('/result',methods=['POST']) 
# def result():
#     global rslt,file
#     if request.method=='POST':
#         # print('pd1')
#         f = request.files['file']
#         filename = secure_filename(f.filename)
#         f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
#         pt = os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER'], filename)
        
#         file = filename

        
#         rslt = calc(pt)
#         print(rslt)
#         print(rslt==1)
        
#         return render_template('result.html',res=rslt,filep=file)
#     else:
#         return "else"



