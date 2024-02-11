from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form action="/ssti">
            <input type="text" name="name" placeholder="Enter your name">
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/ssti')
def ssti():
    name = request.args.get('name', 'World')
    template = f'Hello, {name}!'
    return render_template_string(template)

if __name__ == '__main__':
    app.run(debug=True)