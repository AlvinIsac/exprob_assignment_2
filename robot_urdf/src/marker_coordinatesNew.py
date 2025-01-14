#!/usr/bin/env python3
import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped
from ros2_aruco_interfaces.msg import ArucoMarkers
import time

current_marker_id = 0
last_spin_time = time.time()  
spin_interval = 1.0  

def marker_callback(msg):
    global current_marker_id
    msg_aruco = msg
    #print("hello from the sub")
    if current_marker_id != msg_aruco.marker_ids[-1]:
        current_marker_id = msg_aruco.marker_ids[-1]
    
    #return current_marker_id 

def create_pose_stamped(navigator, position_x, position_y, yaw):
    goal_pose = PoseStamped()
    goal_pose.header.frame_id = 'map'
    goal_pose.header.stamp = navigator.get_clock().now().to_msg()
    goal_pose.pose.position.x = position_x
    goal_pose.pose.position.y = position_y
    goal_pose.pose.orientation.z = yaw
    return goal_pose


def main():
    rclpy.init()
    nav = BasicNavigator()
    nav.waitUntilNav2Active()

    node = rclpy.create_node('marker_navigation')
    node.create_subscription(ArucoMarkers, '/aruco_markers', marker_callback, 10)


    goal_pose1 = create_pose_stamped(nav, -2.2, -7.7, -3.0)
    goal_pose2 = create_pose_stamped(nav, 6.8, -5.2, 1.3)
    goal_pose3 = create_pose_stamped(nav, 5.8, 1.9, 2.3)
    goal_pose4 = create_pose_stamped(nav, -6.4, 1.4, -2.4)

    marker_to_go = {} 
    for i in range(1,5):
        goal_pose = eval(f"goal_pose{i}")
        nav.goToPose(goal_pose)
        while not nav.isTaskComplete():
            #rclpy.spin_once(node)
            #current_time = time.time()
            #if current_time - last_spin_time >= spin_interval:
                #rclpy.spin_once(node)  # Process callbacks
                #last_spin_time = current_time 
            #feedback = nav.getFeedback()
            pass

        rclpy.spin_once(node)
        print(nav.getResult())
        marker_to_go[f"goal_pose{i}"] = current_marker_id    
        print(marker_to_go)

    lowest_id = min(marker_to_go, key=marker_to_go.get)
    lowest_goal = marker_to_go[lowest_id]
    print(f"Lowest Id from all the markers is: {lowest_goal}, its {lowest_goal}")
    #print("look below ")
    #print(lowest_goal)

    nav.goToPose(eval(lowest_id))
    while not nav.isTaskComplete():
        pass

    print(nav.getResult())
    print("Reached the lowest id of all marker!!")
    rclpy.shutdown()

if __name__ == '__main__':
    main()
