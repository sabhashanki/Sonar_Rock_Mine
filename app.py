from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)

model = pickle.load(open('sonar.pkl','rb'))

@app.route('/')
def home():
    return 'Lets see whether you gonna live or not'

@app.route('/predict', methods = ['POST'])
def predict():
    df = pd.read_csv(request.files.get('file'))
    prediction = model.predict(df)
    return 'Predicted values for the file is' + str(list(prediction))


if __name__ == '__main__':
    app.run()