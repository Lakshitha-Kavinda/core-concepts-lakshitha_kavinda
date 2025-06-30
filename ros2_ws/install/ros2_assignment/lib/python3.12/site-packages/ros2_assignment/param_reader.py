import rclpy
from rclpy.node import Node

class ParamReader(Node):
    def __init__(self):
        super().__init__('param_reader')
        self.declare_parameter('robot_name', 'unknown')
        name = self.get_parameter('robot_name').get_parameter_value().string_value
        self.get_logger().info(f"Robot name: {name}")

def main(args=None):
    rclpy.init(args=args)
    node = ParamReader()
    rclpy.shutdown()
