
import numpy as np
from flask import Flask, request, render_template
import pickle

# flask app
app = Flask(__name__)
# loading model
model = pickle.load(open('model2.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('Index.html')
@app.route('/prediction' ,methods = ['POST'])
def prediction():
    final_features = [int(x) for x in request.form.values()]
    final_features = [np.array(final_features)]
    prediction = model.predict(final_features)

    return render_template('Index.html', output='Child Behavioral Wellbeing Status is :  {}'.format(prediction[0]))

if __name__ == "__main__":
    app.run(debug=True,use_reloader=False)