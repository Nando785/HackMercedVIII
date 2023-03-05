from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

compName = {}

@app.get('/')
def home():
    return render_template('index.html', html_compName = compName)

@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        index = len(compName) + 1
        compName[index] = request.form.get('companyName')
        print(compName)
        return redirect(url_for('home'))
    return render_template('add.html')
