import requests

'''
Test Script for Telemarketing Campaign Success Prediction Model

Below you can find a sample customer that will get a prediction if a telemarketing campaign will succeed or not.

You can tweak the values of this customer to get a positive or negative anwer from the prediction service, 
for this the most important features are:
- age: Play with values from 20 to 50 and you will see the difference
- poutcome: Play with these values: "failure","nonexistent","success"
- previous: Play with values from 0 to 10

'''

customer = {
    'age': 30,
    'job': 'admin_',
    'marital': 'single',
    'education': 'university_degree',
    'default': 'no',
    'housing': 'no',
    'loan': 'yes',
    'contact': 'cellular',
    'month': 'oct',
    'day_of_week': 'tue',
    'campaign': 1,
    'pdays': 0,
    'previous': 0,
    'poutcome': 'success',
    'emp_var_rate': 1.4,
    'cons_price_idx': 93.444,
    'cons_conf_idx': -36.1,
    'euribor3m': 4.966,
    'nr_employed': 5228.1
}

customer

url = 'http://0.0.0.0:9696/predict'

result = requests.post(url, json=customer).json()

if result['mkt_success'] == 1.0:
    print('Its Ok to go ahead with telemarketing campaign to client')
else:
    print("Dont go ahead with telemarketing campaign to client")


