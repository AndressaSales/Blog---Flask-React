from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def pag_home():
    user = [
        {"Nome": "Python"},
        {"Nome": "Python"},
        {"Nome": "Python"},
        {"Nome": "Python"},
        {"Nome": "Python"},
        {"Nome": "Python"},
        {"Nome": "Python"},
        {"Nome": "Python"},
        {"Nome": "Python"},
        {"Nome": "Python"},
        {"Nome": "Python"}
    ]
    return render_template('index.htmal', x=user)

app.run(debug=True)