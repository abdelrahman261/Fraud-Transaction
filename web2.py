from flask import Flask, request, jsonify, render_template
import json
import joblib

app = Flask(__name__)

@app.route('/predict2', methods=['POST'])
def test2():
    client=list(request.json.values())
    model3=joblib.load('model3.pkl')
    scaler=joblib.load('scaler.pkl')
    client=scaler.transform([client])
    predict=int(model3.predict(client)[0])
    if model3.predict(client)[0]==0:
        
        return jsonify('NOT--FRAUD!!')
        
    else: 
        
        return jsonify('FRAUD!!')



app.run(debug=True)