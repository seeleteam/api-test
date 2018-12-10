import json
from flask import Flask
from flask import jsonify
from flask import request
from websocket import create_connection

app = Flask(__name__)


ws = create_connection("ws://117.50.16.154:8000/ws")
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
    data = request.get_json()
    print(data)
    ws.send(json.dumps(data))
    result = ws.recv()

    return jsonify(json.loads(result))

if __name__ == '__main__':
    app.run(debug=True)
