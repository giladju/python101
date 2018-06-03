import uuid

class Message:
    def __init__(self,id,content):
        self.id = id
        self.content = content

class MessageStore:
    messages = []

    def __init__(self):
        print("message store created")


    def add_message(self,content):
        id = str(uuid.uuid1())
        self.messages.append(Message(id, content))
        print('New message uuid: ' + id + " with content: " + content)
        return id

    def get_message(self,id):
        print('Getting message by ID: ' + id)
        current_message = [msg for msg in self.messages if msg.id == id]
        # print('#################################')
        # print("Message is: " + str(current_message[0].content))
        # print('#################################')

        return current_message[0]


message_store = MessageStore()

id = message_store.add_message('testing123')

print(id)

message = message_store.get_message(id)

print(message.content)