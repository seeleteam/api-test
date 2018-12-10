from websocket import create_connection
ws = create_connection("ws://117.50.16.154:8000/ws")
payload = """
{
  "jsonrpc": "2.0",
  "method": "seele_getInfo",
  "params": [],
  "id": 1
}
"""
ws.send(payload)
result =  ws.recv()
print("Received '%s'" % result)
ws.close()
