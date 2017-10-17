import os
from setuptools import setup


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name="vocab_trainer",
    version="0.0.1",
    author="Hendrik Müller",
    author_email="henne90gen@gmail.com",
    packages=['vocab_trainer'],
    install_requires=['cement'],
    long_description=read('README.md'),
    description="Command line application for practicing vocabulary",
    # license="BSD",
    # keywords="example documentation tutorial",
    # url="http://packages.python.org/an_example_pypi_project",
    # classifiers=[
    #     "Development Status :: 3 - Alpha",
    #     "Topic :: Utilities",
    #     "License :: OSI Approved :: BSD License",
    # ],
)
