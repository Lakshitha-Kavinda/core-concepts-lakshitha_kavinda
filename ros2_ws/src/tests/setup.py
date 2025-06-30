from setuptools import setup

package_name = 'tests'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lakshitha',
    maintainer_email='your@email.com',
    description='Test publisher/subscriber nodes',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'chatter.py = tests.chatter:main',
            'listener.py = tests.listener:main',
        ],
    },
)

