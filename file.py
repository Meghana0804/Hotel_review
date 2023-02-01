# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 19:09:58 2023

@author: megha
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 19:13:36 2020

@author: bvv
"""

from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np


app = Flask(__name__)
model_pkl = pickle.load(open('final.pkl', 'rb'))
#print(type(model))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
   To get values from HTML user as input
    '''
    int_ft = [int(x) for x in request.form.values()]
    print(int_ft)
    final_ft = [np.array(int_ft)]
    print(final_ft)
    final_prediction = model_pkl.predict(final_ft)
    #print(final_prediction)
    final_values = round(final_prediction[0], 2)

    return render_template('index.html', prediction_text='Rating is  {}'.format(final_values))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    To get results by predict api
    '''
    data_values = request.get_json(force=True)
    final_prediction = model_pkl.predict([np.array(list(data_values.values()))])

    final_values = final_prediction[0]
    return jsonify(final_values)

if __name__ == "__main__":
    app.run(debug=False)
