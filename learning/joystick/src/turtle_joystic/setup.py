from setuptools import find_packages, setup

package_name = 'turtle_joystic'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kol',
    maintainer_email='kolkemboi@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "joy_stick_listener = turtle_joystic.joystick_listener:main",
            "turtle_controller = turtle_joystic.turtle_cont:main",
        ],
    },
    package_data={
        package_name: ['launch/*.launch.py'],  # Include all launch files
    },
)
