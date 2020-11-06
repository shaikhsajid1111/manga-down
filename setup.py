import setuptools

with open("README.md","r") as file:
    long_description = file.read()

setuptools.setup(
    name = "manga_down",
    version = "0.1.1",
    author = "Shaikh Sajid",
    author_email = "shaikhsajid3732@gmail.com",
    description = "Python package to download manga available on mangareader and mangapanda",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/shaikhsajid1111/manga-down/",
    keywords = "web-scraping manga-down manga-download download manga-downloader requests bs4 beautifulsoup mangreader mangapanda",
    packages = setuptools.find_packages(),
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X", 
       

    ],
    python_requires = ">=3.6.9",
    install_requires=[
        'bs4==0.0.1',
        'requests==2.22.0',
        'fake-headers==1.0.2'
    ])
