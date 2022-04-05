from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    return render_template('contact.html')

@app.route('/submitedForm', methods=['POST','GET'])
def submitedForm():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return render_template('submitedForm.html', name=name, email=email)
    else:
        return "ERROR url reached without using form"

if __name__ == "__main__":
    app.run(debug=True)