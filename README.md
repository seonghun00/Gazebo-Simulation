# Mobile Robot restaurant Simulation

#### English | [한국어](README.ko.md)

![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![ROS2](https://img.shields.io/badge/ROS2-Humble-blue)
![Gazebo](https://img.shields.io/badge/Gazebo-11-orange)

> This repository is created for the purpose of learning ROS 2 and Gazebo simulation.

This project is designed to verify the driving performance and sensor operations of a mobile service robot within a cafe/restaurant environment. It is fully containerized using Docker, allowing you to run the simulation in an identical development environment without requiring a native ROS 2 installation.

---

## 🚧 Project Status

### Roadmap

- [x] Mobile Robot URDF Modeling
- [x] LiDAR Sensor Integration
- [x] Differential Drive Configuration
- [x] Simple Restaurant Environment
- [x] Gazebo Simulation Launch
- [ ] SLAM Mapping
- [ ] AMCL Localization
- [ ] Nav2 Integration
- [ ] Waypoint Navigation
- [ ] Autonomous Serving Scenario
- [ ] RViz Visualization

---

## Preview

### Mobile Robot Model
<img width="1280" height="688" alt="빈월드 서빙로봇" src="https://github.com/user-attachments/assets/7acf06bd-3825-44f7-9a45-ec2eab9c51fa" />

<p align="center"><i>Fig1. servi_model.urdf spawned in an empty world</i></p>

### Restaurant Simulation Environment
<img width="1400" height="784" alt="레스토랑 안 서빙로봇" src="https://github.com/user-attachments/assets/61a68b0c-fcf5-49a2-88d2-f2a917c236b4" />

<p align="center"><i>Fig2. Mobile robot operating within the Gazebo simple restaurant environment</i></p>

---

## Overview

### Features
* Simulation environment based on ROS 2 Humble
* Gazebo Cafe World implementation
* Mobile robot URDF modeling
* 2D LiDAR sensor simulation
* Differential Drive kinematic model application
* Docker-based development environment support

---

## Simulation Components

| Component | Description |
| :--- | :--- |
| **Robot Model** | Mobile Service Robot |
| **Sensor** | 2D LiDAR |
| **Drive System** | Differential Drive |
| **Environment** | Simple Restaurant |
| **Simulator** | Gazebo Classic |
| **Middleware** | ROS 2 Humble |

---

## Project Structure

```text
Gazebo-Simulation/
├── docker-compose.yml
├── Dockerfile
├── README.md
└── ros2_gazebo_ws/
    └── src/
        └── my_robot_package/
            ├── launch/
            │   └── spawn_servi.launch.py
            ├── models/
            │   ├── chair/
            │   ├── counter/
            │   ├── table/
            │   └── table_set/
            ├── urdf/
            │   └── servi_model.urdf
            ├── worlds/
            │   └── simple_restaurant.world
            ├── package.xml
            └── setup.py
```

---

## Requirements

### Host Environment
* Docker Desktop
* Docker Compose

### Simulation Environment
* Ubuntu 22.04
* ROS 2 Humble
* Gazebo 11
* RViz2

---

# How to Use

## 1. Clone Repository

```bash
git clone [https://github.com/seonghun00/Gazebo-Simul.git](https://github.com/seonghun00/Gazebo-Simul.git)
cd Gazebo-Simul
```

## 2. Start XLaunch (For Windows Host)

To enable the Gazebo GUI when running via Docker on a Windows host environment, configure XLaunch with the following settings:

1. Select **Multiple Windows**
2. Set **Display Number** → `0`
3. Select **Start No Client**
4. Check **Disable Access Control**
5. Click **Finish**

## 3. Start Docker Environment

```bash
# Start the container in detached mode
docker-compose up -d

# Attach to the simulation container shell
docker-compose exec robot-sim bash
```

## 4. Build Workspace

Inside the Docker container terminal, execute the following commands to build the ROS 2 workspace:

```bash
cd /workspace/ros2_gazebo_ws

# Clean up previous build artifacts if any
rm -rf build install log

# Build the specific package
colcon build --packages-select my_robot_package

# Source the workspace environment
source install/setup.bash
```

---

# Run Simulation

## 1. Empty World (Robot Model Verification)

This step verifies whether the URDF model loads correctly without any environmental obstacles.

### Terminal 1 (Launch Gazebo Server)
```bash
ros2 launch gazebo_ros gazebo.launch.py
```

### Terminal 2 (Spawn Robot Entity)
```bash
cd /workspace/ros2_gazebo_ws

ros2 run gazebo_ros spawn_entity.py \
  -entity mobile_robot \
  -file src/my_robot_package/urdf/servi_model.urdf
```
*You can verify the URDF structure and visual appearance of the mobile robot model spawned in the empty Gazebo world.*

---

## 2. Restaurant Simulation

This step launches the full integrated simulation setup including both the custom restaurant environment and the mobile robot.

```bash
ros2 launch my_robot_package spawn_servi.launch.py
```
*Upon execution, Gazebo will open up displaying the simple restaurant world with the mobile service robot automatically spawned at its initial position.*

---

© 2026 Seong-hun Bae.
