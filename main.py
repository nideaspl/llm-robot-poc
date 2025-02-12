import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleSimController(Node):
    def __init__(self):
        super().__init__('turtlesim_controller')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.command_mapping = {
            "move forward": {"linear_x": 2.0, "angular_z": 0.0},
            "move backward": {"linear_x": -2.0, "angular_z": 0.0},
            "turn left": {"linear_x": 0.0, "angular_z": 2.0},
            "turn right": {"linear_x": 0.0, "angular_z": -2.0},
            "stop": {"linear_x": 0.0, "angular_z": 0.0}
        }
        self.get_logger().info("Turtlesim Controller Initialized. Type commands to move the turtle.")

    def process_command(self, command):
        """ 根据用户输入的指令，发送对应的 `Twist` 消息 """
        if command in self.command_mapping:
            twist = Twist()
            twist.linear.x = self.command_mapping[command]["linear_x"]
            twist.angular.z = self.command_mapping[command]["angular_z"]
            self.publisher_.publish(twist)
            self.get_logger().info(f"Executed command: {command}")
        else:
            self.get_logger().warn(f"Unknown command: {command}")

def main(args=None):
    rclpy.init(args=args)
    node = TurtleSimController()

    try:
        while rclpy.ok():
            command = input("Enter command (move forward, move backward, turn left, turn right, stop): ").strip().lower()
            node.process_command(command)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
