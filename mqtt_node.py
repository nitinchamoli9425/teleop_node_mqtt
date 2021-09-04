import rclpy
from rclpy.node import Node
import time
from rclpy import qos
from rclpy.qos import QoSProfile
import paho.mqtt.client as mqtt
from geometry_msgs.msg import Twist

import os
import select
import sys

if os.name == 'nt':
    import msvcrt
else:
    import termios
    import tty

class SubcribePublishMQTT(Node):

    def __init__(self):
        super().__init__('subscribe_publish_mqtt')
       # self.publisher_ = self.create_publisher(Twist, 'cmd_vel', qos)
        # timer_period = 0.5  # seconds
        # self.timer = self.create_timer(timer_period, self.timer_callback)
        # self.i = 0
        self.subscription = self.create_subscription(Twist, 'cmd_vel', self.listener_callback, 10)
        self.subscription
        namespace = '',
        parameters = [('host', None), ('port', None)]
        self.host = "broker.hivemq.com"
        self.port = 1883

        # handle exception when no connection
        self.client = mqtt.Client()
        self.client.connect(self.host, self.port)
        self.client.loop_start()
        # self.client.subscribe([("mqtt/topic", 0)])
        # self.client.on_message = self.topic_get
    #     self.when_connected()
    #
    # def when_connected(self):
    #     # self.publish()
    #     self.subscribe()

    # def publish(self):
    #     return
    #
    # def subscribe(self):

    #
    # def topic_get(self, client, userdata, msg):
    #     send = String()
    #     topic = msg.topic
    #     message = str(msg.payload.decode("utf-8"))
    #     send.data = message
    #     print(message)
    #     self.publisher_.publish(send)

    def listener_callback(self, twist):
        # ang = { "angular" : [twist.angular.x, twist.angular.y, twist.angular.z]}
        # lin = { "linear" : [twist.linear.x, twist.linear.y, twist.linear.z]}
        #data = {"angular" : [twist.angular.x, twist.angular.y, twist.angular.z], "linear" : [twist.linear.x, twist.linear.y, twist.linear.z]}
        data1 = str(twist.angular.z)+ ";" + str(twist.linear.x)
        #data = bytearray(data1)
        # print(data)
        self.client.publish("cmd/vel", data1)
    # def timer_callback(self):
    #     msg = String()
    #     msg.data = 'Hello World: %d' % self.i
    #     self.publisher_.publish(msg)
    #     self.get_logger().info('Publishing: "%s"' % msg.data)
    #     self.i += 1


def main(args=None):
    rclpy.init(args=args)

    subscribe_publish_mqtt = SubcribePublishMQTT()

    rclpy.spin(subscribe_publish_mqtt)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    subscribe_publish_mqtt.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
