import asyncio
import websockets
import json

class WSServer(object):
    def __init__(self, port = 8765):
        start_server = websockets.serve(self.run_server, "localhost", port)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
        self.throttle = 0.0
        self.steering = 0.0

    async def run_server(self, websocket, path):
        received_msg = await websocket.recv()
        print(f"< {received_msg}")
        received_msg_json = json.loads(received_msg)
        self.steering = received_msg_json["steering"]
        self.throttle = received_msg_json["throttle"]

def main():
    ws_server = WSServer()

if __name__ == '__main__':
    main()
