from setuptools import setup, find_packages

setup(
    name='mapnik_xml',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'lxml==4.2.5'
    ],
    test_suite='tests'
)