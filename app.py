import os

from datetime import datetime

import pandas as pd
import numpy as np

import joblib
import json
import requests
import warnings
import wsgiserver
import logging

from flask import Flask, jsonify, request, render_template
from repositories.EfarRepository import EfarRepository
from controllers.EfarModelController import EfarModelController
from controllers.EfarScoringController import EfarScoringController
from controllers.EfarCustomerController import EfarCustomerController

warnings.filterwarnings('ignore')
logging.getLogger().disabled = True

app = Flask(__name__, template_folder='templates')
app.config.from_object('config')

repository = EfarRepository('./repositories/data/')
customerController = EfarCustomerController(repository)
scoringController = EfarScoringController(repository)
modelController = EfarModelController(repository)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/customers/')
def customers():
    return customerController.get_customers_references()

@app.route('/predict_form', methods=['POST'])
def predict_form():
    customer_reference = int(request.form['customer_reference'])
    customers_references = customerController.get_customers_references().get_json()['customers_references']
    predicted_proba = f'Customer [{customer_reference}] not found'
    df_scoring = scoringController.get_scoring()
    model = modelController.get_model()

    if str(customer_reference) in customers_references:
        df_customer = df_scoring[df_scoring.index == customer_reference]
        predicted_proba = model.predict_proba(df_customer)[0]
    
    return render_template('index.html', prediction_text=predicted_proba[1])
    
@app.route('/predict/<int:customer_reference>')
def predict(customer_reference):
    customers_references = customerController.get_customers_references().get_json()['customers_references']
    df_scoring = scoringController.get_scoring()
    model = modelController.get_model()
    predicted_proba0 = predicted_proba1 = f'customer [{customer_reference}] not found'
        
    if str(customer_reference) in customers_references:
        df_customer = df_scoring[df_scoring.index == customer_reference]
        predicted = model.predict(df_customer)[0]
        predicted_proba = model.predict_proba(df_customer)[0]
        predicted_proba0 = predicted_proba[0]
        predicted_proba1 = predicted_proba[1]

    return jsonify(
        {
            'customer_reference': customer_reference,
            'predicted' : str(predicted), 
            'predicted_proba0': str(predicted_proba0),
            'predicted_proba1': str(predicted_proba1)
        }
    )

if __name__ == '__main__':
    #app.run()
    server = wsgiserver.WSGIServer(app, host='127.0.0.1', port=5001)
    server.start()
					 