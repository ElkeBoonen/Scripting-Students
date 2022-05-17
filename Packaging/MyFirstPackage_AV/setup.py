from setuptools import setup, find_packages

setup(
    name="firstpackage",
    version="0.1",
    description="This is Herman's package ;) it it a very cool one",
    author="Herman and his dog",
    license="MIT",
    packages=find_packages(include=["firstpackage"]),
    install_requires=[]
)