from flask import Flask, request, jsonify
import pickle
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# Load the model
with open('linear_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Dictionaries to simulate label encoding
customer_name_dict = {}
customer_email_dict = {}
customer_country_dict = {}
payment_method_dict = {}

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        # Extract features
        customer_name = data['Customer Name']
        customer_email = data['Customer Email']
        customer_country = data['Customer Country']
        invoice_amount = float(data['Invoice Amount'])
        payment_method = data['Payment Method']
        payment_due_date = datetime.strptime(data['Payment Due Date'], '%Y-%m-%d')
        payment_date = datetime.strptime(data['Payment Date'], '%Y-%m-%d')
        
        # Simulate label encoding
        if customer_name not in customer_name_dict:
            customer_name_dict[customer_name] = len(customer_name_dict)
        if customer_email not in customer_email_dict:
            customer_email_dict[customer_email] = len(customer_email_dict)
        if customer_country not in customer_country_dict:
            customer_country_dict[customer_country] = len(customer_country_dict)
        if payment_method not in payment_method_dict:
            payment_method_dict[payment_method] = len(payment_method_dict)
        
        customer_name_encoded = customer_name_dict[customer_name]
        customer_email_encoded = customer_email_dict[customer_email]
        customer_country_encoded = customer_country_dict[customer_country]
        payment_method_encoded = payment_method_dict[payment_method]
        
        # Convert dates to numerical format (days since a reference date)
        reference_date = datetime(2000, 1, 1)
        payment_due_date_numeric = (payment_due_date - reference_date).days
        payment_date_numeric = (payment_date - reference_date).days
        
        # Prepare input for model
        input_data = [[customer_name_encoded, customer_email_encoded, customer_country_encoded, 
                       invoice_amount, payment_method_encoded, payment_due_date_numeric, payment_date_numeric]]
        
        # Make prediction
        prediction = model.predict(input_data)
        
        return jsonify({'predicted_delay': float(prediction[0] - 33)})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)