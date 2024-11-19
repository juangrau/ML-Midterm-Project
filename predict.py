#%%
from flask import Flask
from flask import request
from flask import jsonify
import pickle
import xgboost as xgb



model_file = 'model.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('bankmkt')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    X = dv.transform(customer)
    features = list(dv.get_feature_names_out())
    dX = xgb.DMatrix(X, feature_names=features)
    y_pred = model.predict(dX)
    go_mkt = y_pred >= 0.5
    
    result = {
        'go_mkt_probability': float(y_pred),
        'go_mkt': bool(go_mkt)
    }

    return jsonify(result)

@app.route('/ping', methods=['GET'])
def ping():
    return 'PONG'

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)

