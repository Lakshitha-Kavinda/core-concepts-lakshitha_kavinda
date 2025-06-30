import rclpy
from rclpy.node import Node

class ParamsSetter(Node):
    def __init__(self):
        super().__init__('params_setter')
        param = 'robot_speed'
        value = 1.5
        self.declare_parameter(param, value)
        self.get_logger().info(f"Set parameter {param} to {value}")

def main(args=None):
    rclpy.init(args=args)
    node = ParamsSetter()
    rclpy.shutdown()
