from setuptools import setup, find_packages

setup(
    name='FastGen',
    version='0.0.1',
    packages=find_packages(),
    package_data={'FastGen': ['templates/*']},
    install_requires=[
        'Jinja2',
    ],
    entry_points={
        'console_scripts': [
            'fastgen=FastGen:main',
        ],
    },
)
