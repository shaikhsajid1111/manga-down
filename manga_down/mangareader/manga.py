try:
    from .chapter_reader import Chapter_reader
    import os
except Exception as ex:
    print(ex)


class Manga(Chapter_reader):
    def __init__(self,manga):
        self.manga = manga
        self.URL = f"http://www.mangareader.cc/manga/{self.URLify(self.manga)}"
    
   