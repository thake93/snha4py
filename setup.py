import setuptools
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setuptools.setup(
    name="snha4py",  # Replace with your own username
    version="0.0.4",
    author="Tim Hake",
    author_email="timhake@icloud.com",
    description="St. Nicholas House algorithm for Python",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/thake93/snha4py",
    project_urls={
        "Documentation": "https://htmlpreview.github.io/?https://github.com/thake93/snha4py/blob/main/docs/__init__.html"
    },
    packages=["snha4py"],
    license="MIT License",
    license_files=["LICENSE"],
    # classifiers=[
    #    "Programming Language :: Python :: 3",
    #    "License :: OSI Approved :: MIT License",
    #    "Operating System :: OS Independent",
    # ],
    install_requires=[
        "numpy>=1.21.3",
        "igraph>=0.9.11",
        "pandas>=1.3.4",
        "matplotlib>=3.4.3",
    ],
)
