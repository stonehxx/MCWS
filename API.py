def reception(message):
    header = message["header"]
    body = message["body"]
    print(header)
    print(body)
    return ""

def send(message,mode,data):
    DATA = {}
    DATA["header"] = header(message)
    if mode == 0:
        DATA["body"] = body_rule(data)
    if mode == 1:
        DATA["body"] = body_command(data)
    return DATA

def header(message):
    DATA = {}
    DATA["requestId"] = "00000000-0000-0000-0000-000000000000"
    DATA["messagePurpose"] = message
    DATA["version"] = 1
    DATA["messageType"] = "commandRequest"
    return DATA

def body_rule(rule):
    DATA = {"eventName" : rule}
    return DATA

def body_command(command):
    DATA = {}
    DATA["origin"] = {}
    DATA["origin"]["type"] = "player"
    DATA["commandLine"] = command
    DATA["version"] = 1
    return DATA