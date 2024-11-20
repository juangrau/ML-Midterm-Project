import requests

'''
Description of the Script
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
    'poutcome': 'nonexistent',
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


