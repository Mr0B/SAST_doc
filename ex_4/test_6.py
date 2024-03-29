from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == 'password':
        return 'Login successful. Welcome, admin!'
    else:
        return 'Invalid credentials. Please try again.'

if __name__ == '__main__':
    app.run(debug=True)