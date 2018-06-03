messages = []

count = 0

def new_message(message_content):
    global count
    count += 1
    print(count)
    messages.append({'id':str(count), 'message':message_content})
    return message_content

def get_message(msg_id):
    current_message = ([d for d in messages if d['id'] == msg_id])
    print('#################################')
    print(current_message)
    print('#################################')
    message_body = (current_message[0].get('message'))
    return message_body