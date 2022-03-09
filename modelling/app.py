from flask import Flask, render_template,request
import sklearn
import joblib
from models.predictionclass import predictclass
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict', methods = ['POST'])
def predict():
	if request.method == 'POST':
		comment = request.form['comment']
		data = [comment]

		my_prediction = predictclass(str(data[0]))

	return render_template('result.html', prediction = my_prediction[0])


if __name__ == '__main__':
	app.run()
