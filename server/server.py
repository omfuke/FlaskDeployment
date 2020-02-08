from flask import Flask,jsonify,request
app = Flask(__name__)
import util

@app.route('/hello',methods = ['GET'])
def get_locations_name():
    response = jsonify({'locations': util.get_locations_names()})
    return response

@app.route('/predict_home_price',methods= ['GET','POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])


    response = jsonify({'estimated_price':util.get_estimated_price(location,total_sqft,bhk,bath)
                        })

    return response

if __name__ == '__main__':
    print('Starting Server.....')
    util.load_artifacts()
    app.run()

