from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        user_input = request.form['text']
        url = 'http://sentimentreview.eastus.azurecontainer.io:8001/predict_probability'
        response = requests.post(url, json={"review": user_input})
        prediction = response.json()

    return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
