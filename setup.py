from setuptools import setup, find_packages

setup(
    name='teemq',
    version='1.0.0',
    description='tee to stdout and AMQP broker',
    url='https://github.com/dzeban/teemq',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(),

    install_requires=['kombu==4.0.2'],
    scripts=['teemq']
)
