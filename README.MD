# manga_down
-----------------
manga_down is a tool to download manga from [Mangareader](https://www.mangareader.net) and [Mangapanda](https://http://www.mangapanda.com) 

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger) 
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/) [![Python >=3.6.9](https://img.shields.io/badge/python-3.6.9+-blue.svg)](https://www.python.org/downloads/release/python-376/)

## Installation

```
pip3 install manga-down
```

## How to use?

### Mangareader

#### To view all chapters available for manga

```python
from manga_down import mangareader     #import mangareader from manga_down

naruto = mangareader.Manga("naruto")   #initialize Manga class with manga name
naruto.get_chapter_list()        #returns list of all chapters of given manga
```

Found the chapter number that you wanted to download?.
Here's how to download that chapter

```python
naruto.download_chapter("120")  #just call the download_chapter by passing chapter number as argument
```

wanted to download the chapter in another folder?
```
file_location = "/home/user/Downloads"
naruto.download_chapter("120", file_location)#this will download the chapter in another folder passed as parameter 
```

----------------------------------------

### Mangapanda

#### To view all chapters available for manga

```python
from manga_down import mangapanda   #import mangapanda from manga_down

bleach = mangapanda.Manga("bleach")   #initialize Manga class with manga name
bleach.get_chapter_list()        #returns list of all chapters of given manga
```

Found the chapter number that you wanted to download?.
Here's how to download that chapter

```python
bleach.download_chapter("120")  #just call the download_chapter by passing chapter number as argument
```

wanted to download the chapter in another folder?
```
file_location = "/home/user/Downloads"
bleach.download_chapter("120", file_location)#this will download the chapter in another folder passed as parameter 
```


### Found something unusual? Report [here](https://github.com/shaikhsajid1111/manga-down/issues)


## LICENSE
[MIT](LICENSE)

