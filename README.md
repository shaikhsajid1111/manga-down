# Manga Down

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/shaikhsajid1111/manga-down/graphs/commit-activity)
[![Python 3.7.6](https://img.shields.io/badge/python-3.7.6-blue.svg)](https://www.python.org/downloads/release/python-376/)





Manga down downloads all mangas available from [mangareader](http://mangareader.net),[mangapanda](http://mangapanda.com),[mangaduck](http://mangapanda.net) and mangarock



## Features:
- Download by chapter number and manga
- Download all chapter just by providing the manga name


## Installation
1. Install dependencies from [requirements](requirements.txt)

1. Go to any folder from project's directory(only works with chrome webdriver)
    - To download chapter of manga:
      - Open terminal in that folder and type ```python image_downloader.py chapter_number 'manga_name'```, Where ```chapter_number``` will be an integer, ```manga_name``` is string(pass under quotation).

1. To download all chapter of manga (only available for manga_reader and mangapanda)
    - Go to either manga_reader or mangapanda folder and open terminal in same, type ```python image_downloader.py 'manga_name'```



## Tech

- [Requests](https://requests.readthedocs.io/en/master/)
- [bs4](https://pypi.org/project/beautifulsoup4/)
- [Selenium](https://selenium-python.readthedocs.io/getting-started.html)

## Demo

![Demo](screenshots/converttogif.gif)