class Author:
    all =[]
    def __init__(self ,name):
        self.name = str(name)
        Author.all.append(self)
    def contracts(self):
        return[contract for contract in Contract.all if contract.author ==self]
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    def sign_contract(self,book, date, royalties):
        return Contract(self,book, date , royalties)
    def  total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())   


class Book:
    all = []
    def __init__(self ,title):
        self.title = str(title)
        self._authors = []
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if self == contract.book]
    
    def authors(self):
        return [author for author in Author.all]  
    def add_author(self,author):
        if isinstance(author,Author):
            self._authors.append(author)
        else: raise TypeError("Author must be of type Author")



class Contract:
    all =[]
    def __init__(self ,author,book,date,royalties):
        self._author = None
        self.author = author
        self._book = None
        self.book = book
        self._date = None
        self.date = date
        self.royalties=int(royalties)
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,value):
        if isinstance(value, Author):
            self._author = value
        else: 
            raise Exception("Author must be of type Author")

    @property
    def book(self):
        return self._book
    @book.setter
    def book(self,value):
        if isinstance(value, Book):
            self._book = value
        else: 
            raise Exception("Book must be of type Book")

    @property
    def date(self):
        return self._date
    @date.setter
    def date(self,value):
        if isinstance(value, str):
             self._date = value
        else:
            raise Exception ("Date must be of type str.")
        
    @classmethod
    def contracts_by_date(cls,date):
        return [contract for contract in cls.all if contract.date == date]
       

        
    


       