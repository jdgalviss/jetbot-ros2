import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from jetbot import Robot

wheelbase = 0.10
wheel_radius = 0.03

class SpeedController(Node):
    def __init__(self, port=8765):
        super().__init__('ws_server')
        self.cmd_sub_ = self.create_subscription(
            Twist, 'jetbot/cmd', self.cmd_callback, 10)
        self.cmd_sub_  # prevent unused variable warning
        self.robot = Robot()

    def inverse_diff_kinematics(self, vel, yaw_rate):
        vel = vel/30.0
        yaw_rate = -yaw_rate/15.0
        if vel == 0.0:
            yaw_rate = yaw_rate * 2.0
        wheel_speed_l = (2*vel-wheelbase*yaw_rate) / (2*wheel_radius)
        wheel_speed_r = (2*vel+wheelbase*yaw_rate) / (2*wheel_radius)
        return wheel_speed_l, wheel_speed_r

    def cmd_callback(self, msg):
        vel_ref = msg.linear.x
        yaw_rate_ref = msg.angular.z
        if(vel_ref < 0.0):
            yaw_rate_ref = -yaw_rate_ref
        wheel_speed_l, wheel_speed_r = self.inverse_diff_kinematics(
            vel_ref, yaw_rate_ref)
        print("wl: {}".format(wheel_speed_l))
        self.robot.set_motors(wheel_speed_r, -wheel_speed_l)


def main(args=None):
    print('Hi from speed_controller.')
    rclpy.init(args=args)
    speed_controller = SpeedController()
    rclpy.spin(speed_controller)

    speed_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
