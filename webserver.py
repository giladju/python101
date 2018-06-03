from flask import Flask
from flask import request
from messages import Message, MessageStore

message_store = MessageStore()

app = Flask(__name__)
# print(app)
@app.route("/")
def hello():
    return "Hello World!"
@app.route("/other")
def different():
    return 'A different world'
@app.route("/message", methods = ['GET'])
def get_message():
    msg_id = request.args.get('message_id')
    msg = message_store.get_message(msg_id)
    return '''<h1>Message ID is: {}</h1>
    <h1>Message Content is: {}</h1>'''.format(msg.id, msg.content)

@app.route("/message", methods=['POST'])
def add_message():
    msg_content = request.form.get('new_message')
    new_id = message_store.add_message(msg_content)
    return '''There is a new Message, ID: {}'''.format(new_id)

@app.route("/all_messages")
def all_messages():
    return '''These are all the mesages:
    {}'''.format(message_store.messages)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port=5000)
