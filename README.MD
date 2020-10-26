# manga-down
-----------------
Download manga from [Mangareader](https://www.mangareader.net) and [Mangapanda](https://http://www.mangapanda.com) 

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger) 
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://pypi.python.org/pypi/ansicolortags/) [![Python >=3.6.9](https://img.shields.io/badge/python-3.6.9+-blue.svg)](https://www.python.org/downloads/release/python-376/)

## Installation
```
pip3 install manga_down
```

## How to use?

### Mangareader

#### To view all chapters available for manga

```python
from manga_down import mangareader

naruto = mangareader.Manga("naruto")   #initialize Chapter_list class with manga name
print(naruto.get_chapter_list())        #prints out all chapter list of naruto manga
```

Found the chapter that you wanted to download?.
Here's how to download that chapter

```python
naruto.download_chapter("120")  #just call the download_chapter by passing chapter number as argument
```

wanted to download the chapter in another folder?
```
file_location = "/usr/Downloads"
naruto.download_chapter("120", file_location)#this will download the chapter on another folder passed as parameter 
```



## LICENSE
[MIT](LICENSE)

