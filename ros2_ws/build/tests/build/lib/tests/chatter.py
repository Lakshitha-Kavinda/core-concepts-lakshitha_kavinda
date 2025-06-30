import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Chatter(Node):
    def __init__(self):
        super().__init__('chatter')
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello from chatter!'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    node = Chatter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

