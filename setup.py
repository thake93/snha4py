import setuptools

setuptools.setup(
    name="snha4py",  # Replace with your own username
    version="0.0.4",
    author="Tim Hake",
    author_email="thake@uni-potsdam.de",
    description="St. Nicholas House algorithm for Python",
    url="https://github.com/thake93/snha4py",
    packages=["snha4py"],
    license="LICENSE",
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
