try:
    from .chapter_reader import Chapter_reader
except Exception as ex:
    print(ex)


class Manga(Chapter_reader):
    def __init__(self,manga):
        self.manga = manga
        self.URL = f"https://mangapark.net/manga/{self.URLify(self.manga)}/"
    
    