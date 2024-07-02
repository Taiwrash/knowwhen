# About Knowwhen

[Video Demo](https://youtu.be/Ntp2OrcMTtE)<br/>
[Landing Page](https://knowwhen.vercel.app)

Knowwhen is an AI-powered infrastructure that predicts invoice payment dates for invoices created on Request Finance. It utilizes a machine learning model trained on historical invoice data and can be integrated into various platforms.

## Overview

Knowwhen is designed to:
- Predict when an invoice will be paid based on historical data
- Integrate seamlessly with different platforms
- Provide accurate payment date estimations for better financial planning

## Technical Stack

- Data - Request Finance Invoice Data
- Machine Learning
- API Framework: Flask
- Testing: Postman

## Usage

- Two ways:
1. Test on Notebook
> Open the notebook, run the notebook and go to the bottom to run `model.predict` providing your data
2. Clone the repository, install all necessary packages and run `python3 app.py`

Example API call:

```python
import requests

url = "http://your-api-endpoint/predict"
payload = {
    "invoice_data": {
       "Customer Name": "James Hall",
      "Customer Email": "zfisher@example.net",
      "Customer Country": "Paraguay",
      "Invoice Amount": 7577.91,
      "Payment Method": "Request",
      "Payment Due Date": "2024-04-11",
      "Payment Date": "2024-05-01"
    }
}
response = requests.post(url, json=payload)
predicted_payment_date = response.json()

```
["predicted_date"]<img width="1440" alt="Screenshot 2024-07-02 at 09 13 09" src="https://github.com/Taiwrash/knowwhen/assets/49725691/e48dfc6e-92df-4681-a560-f16a73c3cb8e">


## Model Training

The machine learning model is trained on historical invoice data from Request Finance. [Add more details about the training process, data preprocessing, and model architecture]

## Testing

The API has been tested using Postman. [Provide instructions on how to run tests or access test results]

## Contact

[Ask us any thing](rasheedrtm1@gmail.com)
