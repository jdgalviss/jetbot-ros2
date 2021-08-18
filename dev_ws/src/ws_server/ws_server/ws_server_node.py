import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import asyncio
import websockets
import json
import os

HOST_IP = os.getenv('HOST_IP', "0.0.0.0")
# WS_SERVER_ADDRESS = "192.168.0.167"
#WS_SERVER_ADDRESS = "localhost"


class WSServerNode(Node):
    def __init__(self, port=8765):
        super().__init__('ws_server')

        # Speed commands publisher (commands are received by WS server)
        self.cmd_publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
        # Start WS Server and loop
        start_server = websockets.serve(
            self.run_server, HOST_IP, port)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

    async def run_server(self, websocket, path):
        # callback when cmd msg is received through WS
        received_msg = await websocket.recv()

        # Unpack info from json
        received_msg_json = json.loads(received_msg)
        steering = received_msg_json["steering"]
        throttle = received_msg_json["throttle"]
        print(steering)
        # Cmd values into msg and publish
        cmd_msg = Twist()
        cmd_msg.linear.x = float(throttle)
        cmd_msg.angular.z = float(steering)
        self.cmd_publisher_.publish(cmd_msg)


def main(args=None):
    print('Hi from ws_server.')
    rclpy.init(args=args)
    ws_server = WSServerNode()
    rclpy.spin(ws_server)

    ws_server.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
