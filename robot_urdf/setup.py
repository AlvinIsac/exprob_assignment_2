from setuptools import setup, find_packages

package_name = 'robot_urdf'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='A package for testing ROS 2 executables.',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'rotate_robot = src.rotate_robot:main',
            'new_follow = src.marker_coordinatesNew:main',
            'old_follow = src.marker_coordinates:main',
        ],
    },
)

