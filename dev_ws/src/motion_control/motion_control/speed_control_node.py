import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

import os
IS_LOCAL = os.getenv('IS_LOCAL', False)
if not IS_LOCAL:
    from jetbot import Robot

wheelbase = 0.10
wheel_radius = 0.02
KF_TURN = 0.5 #0.5
KP_TURN = 0.1
KI_TURN = 0.05#0.0001

KF_FWD = 0.2# vel
KP_FWD = 0.2
KI_FWD = 0.1#0.0001

class SpeedController(Node):
    def __init__(self, port=8765):
        super().__init__('ws_server')
        self.cmd_sub_ = self.create_subscription(Twist, 'cmd_vel', self.cmd_callback, 10)
        self.odom_sub_ = self.create_subscription(Odometry, 'rs_t265/odom', self.odom_callback, 10)
        self.vel_cmd_ = 0.0
        self.yaw_rate_cmd_ = 0.0

        self.yaw_rate_error_int_ = 0.0
        self.vel_error_int_ = 0.0
        if not IS_LOCAL:
            self.robot = Robot()
            
    def inverse_diff_kinematics(self, vel, yaw_rate):
        vel = vel #/30.0
        if(self.vel_cmd_ == 0.0):
            yaw_rate *= 4.5 #/-15.0
            vel = 0.0
            self.vel_error_int_ = 0.0
        if(self.yaw_rate_cmd_ == 0.0):
            self.yaw_rate_error_int_ = 0.0
            yaw_rate = 0.0

        if vel == 0.0:
            yaw_rate = yaw_rate
        wheel_speed_l = (2*vel-wheelbase*yaw_rate) / (2*wheel_radius)
        wheel_speed_r = (2*vel+wheelbase*yaw_rate) / (2*wheel_radius)
        return wheel_speed_l/10.0, wheel_speed_r/10.0

    def odom_callback(self, msg):

        vel = msg.twist.twist.linear.x
        yaw_rate = msg.twist.twist.angular.z
        # Long. speed control
        error = (self.vel_cmd_ - vel)
        if (abs(self.vel_error_int_) < 100.0): self.vel_error_int_ += error
        vel_out = KF_FWD*self.vel_cmd_ + KP_FWD*(error + KI_FWD*self.vel_error_int_ )

        # Yaw rate control
        error = self.yaw_rate_cmd_ - yaw_rate
        if (abs(self.yaw_rate_error_int_) < 100.0): self.yaw_rate_error_int_ += error
        yaw_rate_out = KF_TURN*self.yaw_rate_cmd_ + KP_TURN*(error + KI_TURN*self.yaw_rate_error_int_)
        wheel_speed_l, wheel_speed_r = self.inverse_diff_kinematics(vel_out, -yaw_rate_out)
        # print('vel: {}, vel_cmd: {} , vel_out: {}'.format(vel,self.vel_cmd_,vel_out))
        # print('w: {}, w_cmd: {} , w_out: {}'.format(yaw_rate,self.yaw_rate_cmd_,yaw_rate_out))
        if not IS_LOCAL:
            self.robot.set_motors(wheel_speed_r, -wheel_speed_l)
        



    def cmd_callback(self, msg):
        vel_ref = msg.linear.x
        yaw_rate_ref = msg.angular.z
        if(vel_ref < 0.0):
            yaw_rate_ref = -yaw_rate_ref
        self.yaw_rate_cmd_  = yaw_rate_ref
        self.vel_cmd_  = vel_ref
        

def main(args=None):
    print('Hi from speed_controller.')
    rclpy.init(args=args)
    speed_controller = SpeedController()
    rclpy.spin(speed_controller)

    speed_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
