from flask import Flask

app = Flask(__name__)
# print(app)
@app.route("/")
def hello():
    print ('DEBUG: Hello World')
    return "Hello World!"
@app.route("/other")
def different():
    print ('DEBUG: A different world')
    return 'A different world'
