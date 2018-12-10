import json
import ast
from flask import Flask
from flask import jsonify
from flask import request
from websocket import create_connection

app = Flask(__name__)



#payload = """
#{
#  "jsonrpc": "2.0",
#  "method": "seele_getInfo",
#  "params": [],
#  "id": 1
#}
#"""
#ws.send(payload)
#result =  ws.recv()
#print("Received '%s'" % result)
#ws.close()

@app.route("/", methods=["POST"])
def index():
    ws = create_connection("ws://117.50.16.154:8000/ws")
    data = request.get_json()
    #payload = ast.literal_eval(json.dumps(data))
    #payload = json.loads(data)
    #print(payload)
    payload = json.dumps(data)
    print(payload)
    print(type(payload))
    ws.send(payload)
    result = ws.recv()
    print("result >>>{}<<<".format(result))

    return jsonify(json.loads(result))

if __name__ == '__main__':
    app.run(debug=True)
