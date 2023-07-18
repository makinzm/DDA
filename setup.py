from setuptools import setup, find_packages

with open('requirements-dev.lock', 'r') as lockfile:
    packages = []
    for line in lockfile:
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('-e'):
            package = line.split('==')[0]
            packages.append(package)

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
