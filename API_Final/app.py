from flask import Flask, render_template, request
import pickle
import numpy as np

scaler=pickle.load(open('StandartScaler.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['x1']
    data2 = request.form['x2']
    data3 = request.form['x3']
    data4 = request.form['x4']
    data5 = request.form['x5']
    data6 = request.form['x6']
    data7 = request.form['x7']
    data8 = request.form['x8']
    data9 = request.form['x9']
    data10 = request.form['x10']
    data11 = request.form['x11']
    data12 = request.form['x12']
    data13 = request.form['x13']
    data14 = request.form['x14']
    data15 = request.form['x15']
    data16 = request.form['x16']
    data17 = request.form['x17']
    data18 = request.form['x18']
    data19 = request.form['x19']
    data20 = request.form['x20']
    data21 = request.form['x21']
    data22 = request.form['x22']
    data23 = request.form['x23']
    data24= request.form['x24']
    data25 = request.form['x25']
    data26 = request.form['x26']
    data27 = request.form['x27']
    data28 = request.form['x28']
    data29 = request.form['x29']
    data30 = request.form['x30']

    arr = np.array([[data1, data2, data3, data4,data5, data6, data7, data8,data9, data10, data11, data12, data13, data14,data15, data16, data17, data18,data19, data20, data21, data22, data23, data24,data25, data26, data27, data28,data29, data30,]])
    arr2=scaler.transform(arr)
    pred = model.predict(arr2)
    return render_template('after.html', data=pred)



if __name__ == "__main__":
    app.run(debug=True)


