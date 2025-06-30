import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import csv

class TwistFromDatabase(Node):
    def __init__(self):
        super().__init__('twist_from_database')
        self.publisher = self.create_publisher(Twist, 'twist_from_database', 20)
        timer_period = 0.1  # 10 Hz
        self.timer = self.create_timer(timer_period, self.publish_twist)
        self.lines = self.load_csv()
        self.index = 0

    def load_csv(self):
        with open('values.csv', newline='') as csvfile:
            return list(csv.reader(csvfile))

    def publish_twist(self):
        if self.index >= len(self.lines):
            return
        values = list(map(float, self.lines[self.index]))
        twist = Twist()
        twist.linear.x, twist.linear.y, twist.linear.z = values[0:3]
        twist.angular.x, twist.angular.y, twist.angular.z = values[3:6]
        self.publisher.publish(twist)
        self.index += 1

def main(args=None):
    rclpy.init(args=args)
    node = TwistFromDatabase()
    rclpy.spin(node)
    rclpy.shutdown()
