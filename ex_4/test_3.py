from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to the vulnerable app!'

@app.route('/redirect')
def redirect_to_url():
    url = request.args.get('url')
    return redirect(url)

if __name__ == '__main__':
    app.run(debug=True)
