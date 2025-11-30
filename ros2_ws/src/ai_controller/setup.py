from setuptools import setup

package_name = 'ai_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sean',
    maintainer_email='you@example.com',
    description='AI controller node using PPO model.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # ros2 run ai_controller ai_node
            'ai_node = ai_controller.ai_node:main',
        ],
    },
)
