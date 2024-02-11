from flask import Flask, request, render_template_string

app = Flask(__name__)
@app.route('/include')
def include_file():
    filename = request.args.get('file')
    content = open(filename, 'r').read()
    return render_template_string(content)

if __name__ == '__main__':
    app.run(debug=True)
