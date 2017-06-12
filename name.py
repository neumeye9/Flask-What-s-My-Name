from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/process', methods= ['POST'])
def firstname():
    print request.form['first_name']
    return redirect('/')

app.run(debug=True)