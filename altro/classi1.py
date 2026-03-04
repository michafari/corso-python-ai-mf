###

class Book:
    def __init__(self, title, subtitle, npages):
        self.title = title
        self.subtitle = subtitle
        self.npages = npages

    def main_infos(self):
        return f"{self.title} : {self.subtitle} has {self.npages} pages"


book1 = Book("Ciao mamma", "sono vivo", 230)
book2 = Book("Ieri piove", "alberi in fiore", 610)

print(book1.main_infos())

