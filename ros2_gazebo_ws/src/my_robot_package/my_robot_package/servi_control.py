
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import sys, select, termios, tty

# Backup terminal settings
settings = termios.tcgetattr(sys.stdin)

msg = """
Servi Custom WASD Control Panel
---------------------------------------
Moving around:
        w
   a    s    d
        x

w / x : Increase linear velocity (Forward / Backward)
a / d : Increase angular velocity (Left / Right)
s     : Emergency Brake (Stop all movement)

CTRL-C to quit
"""

class ServiTeleop(Node):
    def __init__(self):
        super().__init__('servi_teleop')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.linear_vel = 0.0
        self.angular_vel = 0.0

    def publish_twist(self):
        twist = Twist()
        twist.linear.x = float(self.linear_vel)
        twist.angular.z = float(self.angular_vel)
        self.publisher_.publish(twist)

def getKey():
    tty.setraw(sys.stdin.fileno())
    select.select([sys.stdin], [], [], 0)
    key = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def main(args=None):
    rclpy.init(args=args)
    node = ServiTeleop()
    print(msg)

    try:
        while True:
            key = getKey()
            if key == 'w':
                node.linear_vel += 0.2
            elif key == 'x':
                node.linear_vel -= 0.2
            elif key == 'a':
                node.angular_vel += 0.5
            elif key == 'd':
                node.angular_vel -= 0.5
            elif key == 's':
                node.linear_vel = 0.0
                node.angular_vel = 0.0
            elif key == '\x03': # CTRL-C
                break

            node.publish_twist()
            print(f"Current Servi Speed 🏎️ : Linear {node.linear_vel:.1f} m/s | Angular {node.angular_vel:.1f} rad/s\r")

    except Exception as e:
        print(e)
    finally:
        # Stop the robot before shutting down
        twist = Twist()
        node.publisher_.publish(twist)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
