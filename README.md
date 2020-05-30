# Manga Down

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/shaikhsajid1111/manga-down/graphs/commit-activity)
[![Python 3.7.6](https://img.shields.io/badge/python-3.7.6-blue.svg)](https://www.python.org/downloads/release/python-376/)





Manga down downloads all mangas available from [kissmanga](http://kissmanga.com), [mangareader](http://mangareader.net) and [mangapanda](http://mangapanda.com)



## Features:
- Download by chapter number and manga
- Download all chapter just by providing the manga name


## Installation
- Install dependencies from [requirements](requirements.txt)

- Go to any folder from manga_reader,magapanda or kissmanga
    - To download chapter of manga:
      - Open terminal in that folder and type ```python image_downloader.py chapter_number 'manga_name'```, Where ```chapter_number``` will be an integer, ```manga_name``` is string(pass under quotation).

- To download all chapter of manga (only available for manga_reader and mangapanda)
    - Go to either manga_reader or mangapanda folder and open terminal in same, type ```python image_downloader.py 'manga_name'```

- Kissmanga uses selenium webdriver. Install it from [here](https://chromedriver.chromium.org/downloads) 
**Note: Chrome version and webdriver version must be compatible**

## Tech

- [Requests](https://requests.readthedocs.io/en/master/)
- [bs4](https://pypi.org/project/beautifulsoup4/)
- [selenium](https://selenium-python.readthedocs.io/)
- [chrome webdriver](https://chromedriver.chromium.org)



## Screenshots

![Demo](screenshots/mangapanda.gif)