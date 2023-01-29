import json
import API

def first_send(mode,steep):
    DATA = ["PlayerMessage"]
    if mode == 0:
        return len(DATA)
    if mode == 1:
        return json.dumps(API.send("subscribe",0,DATA[steep],0))

def send():
    return ""

def reception(message):
    DATA = json.dumps(message)