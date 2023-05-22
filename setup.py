import setuptools

with open("README.md","r") as file:
    long_description = file.read()

setuptools.setup(
    name = "manga_down",
    version = "0.1.2",
    author = "Shaikh Sajid",
    author_email = "shaikhsajid3732@gmail.com",
    description = "Python package to download manga available on mangareader and mangapanda",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/shaikhsajid1111/manga-down/",
    keywords = "web-scraping manga-down manga-download download manga-downloader requests bs4 beautifulsoup mangreader mangapanda",
    packages = setuptools.find_packages(),
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X", 
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP"
        

    ],
    python_requires = ">=3.6.9",
    install_requires=[
        'bs4==0.0.1',
        'requests==2.31.0',
        'fake-headers==1.0.2'
    ])
