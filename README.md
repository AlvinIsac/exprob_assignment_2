# exprob_assignment_2

## Prerequisites

Ensure you have **ROS 2 Humble** or a higher version recommended.
Gazebo
OpenCV 2

### Install the Dependencies
Run the following commands to install the required ROS 2 packages:

```bash
sudo apt install ros-humble-nav2-simple-commander
sudo apt install ros-humble-tf-transformations
sudo apt install ros-humble-navigation2
sudo apt install ros-humble-nav2-bringup
```

> **Note**: If you are using a version of ROS 2 other than Humble, replace `humble` with your ROS 2 version.

After installing all dependencies, update and upgrade your system:

```bash
sudo apt update
sudo apt upgrade
```

## Cloning the Repository

1. Navigate to your ROS 2 workspace and clone the repository inside the `src` folder:
   ```bash
   cd <your_ros2_workspace>/src
   git clone git@github.com:AlvinIsac/exprob_assignment_2.git
   ```

2. Build the workspace:
   ```bash
   cd ..
   colcon build
   ```

## Running the Project

Open **three terminals** and source your workspace in each terminal:

```bash
source install/setup.bash
```

### Step 1: Launch the Gazebo Simulation
In the first terminal, run:

```bash
ros2 launch robot_urdf gazebo.hw2.launch.py
```

### Step 2: Launch the Navigation Stack
In the second terminal, run:

```bash
ros2 launch nav2_bringup bringup_launch.py map:=/<give_your_path>/src/exprob_assignment_2/robot_urdf/map/map.yaml
```

> **Note**: Replace `<give_your_path>` with the full path to your workspace. Ensure the parameters are set correctly, or the launch may fail.

### Step 3: Execute the Marker Identification Script
In the third terminal, run:

```bash
cd <your_path_to_ws>/src/exprob_assignment_2/robot_urdf/src
./marker_coordinatesNew.py
```

Now, in Gazebo, you will see the robot navigate to all the markers, identify their IDs, and finally move to the marker with the **lowest ID**.

## Testing

Feel free to modify the marker IDs in the Gazebo world to test the robot. While the navigation may take some time, the robot will complete the task as designed.

## Additional Notes

- Ensure all parameters are correctly configured, especially when launching the navigation stack.
- If you encounter any issues, verify the installation of dependencies and confirm the workspace is correctly sourced.

---

Thank you for using this project! Contributions and feedback are welcome.

