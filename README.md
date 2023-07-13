# [5dpo_q2_ros_nav_conf](https://github.com/5dpo/5dpo_q2_ros_nav_conf)

This repository implements the launch files required for the 5DPO Navigation
Stack on the
[Hangfa Discovery Q2](http://www.hangfa.com/EN/robot/DiscoveryQ2.html). The
system implemented is based on the INESC TEC Robotics Navigation Stack that it
allows you to have different configurations implemented and selecting just one
based on your environment variables.

**Version 0.3.0**

**With this version, it is possible to do:**

- ROS package creation (`CMakeLists.txt`, `package.xml`)
- `basic` configuration
- `sim0` configuration (Gazebo-based Simulation)
- `slam3d0` configuration (A-LOAM)

**The next version will add these features:**

- `slam0` configuration ([SLAM Toolbox](https://wiki.ros.org/slam_toolbox))
- `slam1` configuration ([Hector SLAM](https://wiki.ros.org/hector_mapping))
- `slam2` configuration ([GMapping](https://wiki.ros.org/gmapping))
- `slam0sim0feup0` configuration (
  [SLAM Toolbox](https://wiki.ros.org/slam_toolbox) w/ Gazebo-based simulation
  in the [FEUP](https://sigarra.up.pt/feup/en) world environment)
- `slam1sim0feup0` configuration (
  [Hector SLAM](https://wiki.ros.org/hector_mapping) w/ Gazebo-based simulation
  in the [FEUP](https://sigarra.up.pt/feup/en) world environment)
- `slam2sim0feup0` configuration (
  [GMapping](https://wiki.ros.org/gmapping) w/ Gazebo-based simulation
  in the [FEUP](https://sigarra.up.pt/feup/en) world environment)

## ROS

**Current version:**

- [Ubuntu 20.04.5 LTS](https://releases.ubuntu.com/focal/)
- [ROS Noetic](https://wiki.ros.org/noetic)

## Usage

### Setup

```sh
# Robot id
export ROBOT_ID=<id>                # (default: unnamed_robot)
# Configuration
export ROBOT_CONF=<configuration>   # (default: basic)
```

### Compilation

```sh
# Create catkin workspace
mkdir -p ~/catkin_ws/src

# Clone repository
cd ~/catkin_ws/src
git clone git@github.com:5dpo/5dpo_q2_ros_nav_conf.git

# Build
cd ..
catkin build
```

### Launch

```sh
roslaunch sdpo_q2_ros_nav_conf wake_up_almighty_q2.launch
```

## Contacts

If you have any questions or you want to know more about this work, please
contact one of the contributors of this package:

- António Paulo Moreira ([github](https://github.com/apaulomoreira),
  [mail](mailto:amoreira@fe.up.pt))
- Héber Miguel Sobreira ([github](https://github.com/HeberSobreira),
  [gitlab](https://gitlab.inesctec.pt/heber.m.sobreira),
  [mail](mailto:heber.m.sobreira@inesctec.pt))
- Ricardo B. Sousa ([github](https://github.com/sousarbarb/),
  [gitlab](https://gitlab.inesctec.pt/ricardo.b.sousa),
  [mail:inesctec](mailto:ricardo.b.sousa@inesctec.pt),
  [mail:personal](mailto:sousa.ricardob@outlook.com),
  [mail:professor](mailto:rbs@fe.up.pt),
  [mail:student](mailto:up201503004@edu.fe.up.pt))
