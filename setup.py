from setuptools import setup, find_packages

setup(
    name='Shush',

    version='0.1.0',
    packages=find_packages(),
    license='GNU General Public License v3.0',
    long_description=open('README.md').read(),
    install_requires=[
        'spidev',
        'RPi.GPIO',
    ]
)
