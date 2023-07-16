from setuptools import setup, find_packages

setup(
    name='books',
    version='1.0.0',
    author='Nozomi Maki',
    description='Reading Books Management App',
    packages=find_packages(),
    install_requires=packages,
    entry_points={
        'console_scripts': [
            'book = src.main:main',
        ],
    },
)
