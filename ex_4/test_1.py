from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the vulnerable app!"

@app.route('/execute', methods=['GET'])
def execute_command():
    command = request.args.get('command')
    if command:
        output = os.popen(command).read()
        return render_template_string('<pre>' + output + '</pre>')
    else:
        return "No command provided."

if __name__ == '__main__':
    app.run(debug=True)