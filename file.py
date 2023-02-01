# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 19:13:36 2020

@author: bvv
"""

from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np


app = Flask(__name__)
model = pickle.load(open('final.pkl', 'rb'))
#print(type(model))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_ft = [int(x) for x in request.form.values()]
    print(int_ft)
    final_ft = [np.array(int_ft)]
    print(final_ft)
    prediction = model.predict(final_ft)
    #print(prediction)
    final_values = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Rating is  {}'.format(final_values))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data_values = request.get_json(force=True)
    prediction = model.predict([np.array(list(data_values.values()))])

    final_values = prediction[0]
    return jsonify(final_values)

if __name__ == "__main__":
    app.run(debug=False)
