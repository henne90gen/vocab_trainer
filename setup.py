import os
from setuptools import setup


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name="vocab_trainer",
    version="0.0.1",
    author="Hendrik Müller",
    author_email="henne90gen@gmail.com",
    packages=['vocab_trainer', 'tests'],
    install_requires=['cement', 'matplotlib', 'romkan'],
    long_description=read('README.md'),
    description="Command line application for practicing vocabulary",
)
