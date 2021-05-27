from flask import Flask
from flask import request
from apology import *

app = Flask(__name__)

@app.route('/apology', methods=['POST'])
def index():
    name = request.form['name']
    event = request.form['event']
    return apol(name, event)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', 8080)
