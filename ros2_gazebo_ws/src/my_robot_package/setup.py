import os
from glob import glob
from setuptools import setup

package_name = 'my_robot_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name], # 이 부분 덕분에 __init__.py가 있는 폴더를 인식함.
    data_files=[
        # 1. ROS 2 시스템이 이 패키지를 찾을 수 있도록 하는 필수 인덱스 파일
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        
        # 2. package.xml 복사
        ('share/' + package_name, ['package.xml']),
        
        # 3. 주요 디렉터리 내부 파일들 복사 (launch, urdf, worlds, config)
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.world')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='name',
    maintainer_email='email_address@email.com',
    description='Servi robot simulation and control',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # 파이썬 제어 노드 실행 명령어 등록
            # 2. 파이썬 실행 경로 변경 (폴더명.파일명:함수명)
            # 터미널에서 'ros2 run my_robot_package servi_control' 입력 시 작동하게 만듦
            'servi_control = my_robot_package.servi_control:main',
        ],
    },
)