from setuptools import find_packages, setup

package_name = 'sim_diff_drive_vision'

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
    maintainer='fectec',
    maintainer_email='fectec151@gmail.com',
    description='This package implements computer vision algorithms for the CoppeliaSim differential drive simulation robot.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'camera_display = sim_diff_drive_vision.camera_display:main',
            'green_sphere_following = sim_diff_drive_vision.green_sphere_following:main',       
            'sphere_detection = sim_diff_drive_vision.sphere_detection:main'       
        ],
    },
)