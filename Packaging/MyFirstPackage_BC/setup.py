from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1",
    description="My first package",
    author="Me, myself and I",
    license="MIT",
    packages=find_packages(include=["mypackage"]),
    install_requires=[]
)