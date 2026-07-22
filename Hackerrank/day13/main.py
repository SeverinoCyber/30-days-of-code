from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self, title ,author , price):
        super().__init__(title,author)
        self.price = price
    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: {self.price}")

title=input("Introduce el titulo del libro")
author=input("Introduce el nombre del author del libro")
price=int(input("Introduce el precio del libro"))
new_novel=MyBook(title,author,price)
new_novel.display()