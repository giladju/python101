from flask import Flask
from flask import request

app = Flask(__name__)
# print(app)
@app.route("/")
def hello():
    return "Hello World!"
@app.route("/other")
def different():
    return 'A different world'
@app.route("/message", methods = ['GET', 'POST', 'DELETE'])
def message():
    if request.method == 'GET':
        msg_id = request.args.get('message_id')
        msg_content = "Testing 123"
        return '''<h1>Message ID is: {}</h1>
        <h1>Message Content is: {}</h1>'''.format(msg_id, msg_content)
    if request.method == 'POST':
        msg_content = request.form.get('new_message')
        return '''<h1>This is a new Message</h1>
        <h1>Message Content is: {}</h1>'''.format(msg_content)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port=5000)
