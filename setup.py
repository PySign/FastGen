from setuptools import setup, find_packages

setup(
    name='FastGen',
    version='0.0.1',
    packages=find_packages(),
    # package_data={'FastGen': ['templates/*']},
    package_data={'': ['LICENSE'], 'FastGen': ['templates/*']},
    install_requires=[
        'Jinja2',
    ],
    entry_points={
        'console_scripts': [
            'fastgen=FastGen:main',
        ],
    },
    author="JRudransh",
    description="Django style project generation made easy for FastApi",
    license="GNU Lesser General Public License v2.1",
    include_package_data=True,
    # zip_safe=False,
)
