from setuptools import setup, find_packages

setup(
    name='prodigi_metrix',
    version='0.0.1',
    description='A Python library for logging events to ProdigiLink Metrix.',
    author='ProdigiLink',
    email='prodigilink@gmail.com',
    url='https://github.com/Automacene',
    packages=find_packages(),
    install_requires=['httpx'],
    license='MIT',
    keywords=['prodigilink', 'prodigilink metrix', 'ai', 'metrics']
)