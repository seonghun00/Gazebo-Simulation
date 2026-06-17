# 모바일 로봇 간이 레스토랑 시뮬레이션

#### [English](README.md) | Korean

![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![ROS2](https://img.shields.io/badge/ROS2-Humble-blue)
![Gazebo](https://img.shields.io/badge/Gazebo-11-orange)

> 본 저장소는 ROS 2 및 Gazebo 학습을 목적으로 만들어진 repo 입니다. 

본 프로젝트는 카페, 레스토랑 환경에서 서비스 로봇의 주행 및 센서 동작을 검증하기 위해 제작되었습니다. Docker 기반으로 구성하여 별도의 ROS 2 설치 없이 동일한 개발 환경에서 실행할 수 있습니다.

## 🚧 Project Status

### 로드맵

- [x] Mobile Robot URDF 모델링
- [x] LiDAR Sensor 연동
- [x] 구동 시스템 설정
- [x] 간이 레스토랑 월드 생성
- [x] Gazebo 시뮬레이션 실행 (Launch)
- [ ] SLAM 지도 생성 Mapping
- [ ] AMCL 위치 추정 (Localization)
- [ ] Nav2 네비게이션 적용
- [ ] 경유지 (Waypoint) 주행 내비게이션
- [ ] 자율 서빙 시나리오 구현
- [ ] RViz 시각화

## Preview

### Mobile Robot Model
<img width="1280" height="688" alt="image" src="https://github.com/user-attachments/assets/4669417f-c91b-45aa-be82-97bd5f58ad8b" />   

<p align="center"><i>Fig1. 빈 월드에서 생성된 servi_model.urdf</i></p>

### Restaurant Simulation Environment
<img width="1400" height="784" alt="image" src="https://github.com/user-attachments/assets/df643983-58ed-4f1b-93e2-3cfa0f024ed9" />   

<p align="center"><i>Fig2. Gazebo 간이 레스토랑 환경에서 동작하는 모바일 로봇</i></p>

---

## Overview

### Features
* ROS 2 Humble 기반 시뮬레이션 환경
* Gazebo Cafe World 구축
* 모바일 로봇 URDF 모델링
* LiDAR 센서 시뮬레이션
* Differential Drive 구동 모델 적용
* Docker 기반 개발 환경 제공

---

## Simulation Components

| Component | Description |
|------------|------------|
| Robot Model | Mobile Service Robot |
| Sensor | 2D LiDAR |
| Drive System | Differential Drive |
| Environment | Simple Restaurant |
| Simulator | Gazebo Classic |
| Middleware | ROS 2 Humble |

---

## 폴더 구조
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
* Gazebo
* RViz2

---

# How to Use

## 1. 깃허브 파일들 불러오기 (clone)

```bash
git clone https://github.com/seonghun00/Gazebo-Simulation.git
cd Gazebo-Simulation
```

## 2. Start XLaunch

Windows 환경에서 Gazebo GUI를 사용하기 위해 XLaunch를 실행합니다.

1. Multiple Windows 선택
2. Display Number → 0
3. Start No Client 선택
4. Disable Access Control 체크
5. Finish

## 3. Docker 환경 구축

```bash
docker-compose up -d

docker-compose exec robot-sim bash
```

## 4. Build Workspace

```bash
cd /workspace/ros2_gazebo_ws

rm -rf build install log

colcon build --packages-select my_robot_package

source install/setup.bash
```

---

# Run Simulation

## 1. Empty World (Robot Model Verification)

URDF 모델이 정상적으로 생성되는지 확인하기 위한 단계입니다.

### 터미널 1

```bash
ros2 launch gazebo_ros gazebo.launch.py
```

### 터미널 2

```bash
cd /workspace/ros2_gazebo_ws

ros2 run gazebo_ros spawn_entity.py \
  -entity mobile_robot \
  -file src/my_robot_package/urdf/servi_model.urdf
```

빈 Gazebo 환경에 로봇 모델만 생성하여 URDF 구조 및 외형을 확인할 수 있습니다.

---

## 2. Restaurant Simulation

```bash
ros2 launch my_robot_package spawn_servi.launch.py
```

실행 후 Gazebo가 시작되며 간이 레스토랑 환경과 모바일 서비스 로봇이 함께 생성됩니다.

---

© 2026 Seong-hun Bae.
