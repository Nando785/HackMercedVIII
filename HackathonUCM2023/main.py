from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

compName = ""

@app.get('/')
def home():
    return render_template('index.html', html_compName = compName)

@app.route('/add', methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        compName = request.form['companyName']
        print(compName)
        return redirect(url_for('home'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)