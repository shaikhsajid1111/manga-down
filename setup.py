import setuptools

with open("README.md","r") as file:
    long_description = file.read()

setuptools.setup(
    name = "manga-down-shaikhsajid1111",
    version = "1.0",
    author = "Shaikh Sajid",
    author_email = "shaikhsajid3732@gmail.com",
    description = "Python package to download manga",
    long_description_content_type = "text/markdown",
    url = "https://github.com/shaikhsajid1111/manga-down/",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.7",


)