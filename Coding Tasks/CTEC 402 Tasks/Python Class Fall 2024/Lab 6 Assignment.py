from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template('index.html', current_time=current_time)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/tips')
def tips():
    return render_template('tips.html')

if __name__ == '__main__':
    app.run(debug=True)
