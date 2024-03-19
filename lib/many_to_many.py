class Author:
    all = []
    def __init__(self, name):
        self.name = name
        self.books = []
        Author.all.append(self)
    def __repr__(self):
        return f'<Author {self.name}>'
    #? return a list comprehension of all the books using the contract class
    #def book(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    #? returns a list of all the books that the author has written
    def get_books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if contract.author == self])
class Book:
    contracts= []
    def __init__(self, title=None ,author=None):
        self.title = title
        self.author = author
        self.authors = []
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

class Contract:
    all = []
    def __init__(self, author, book,date,royalties):
        if not isinstance(date,str):
            raise Exception('Date must be a string')
        if not isinstance(author, Author):
            raise Exception('Author must be an instance of the Author class')
        if not isinstance(royalties,int):
            raise Exception('Royalties must be an integer')
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties 
        author.books.append(book)
        book.authors.append(author)
        Contract.all.append(self)
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    def get_date(self):
        return self.date
    def set_date(self, date):
            self.date = date
    def contracts_by_date(date):
        return [contract for contract in Contract.all if contract.date == date]
            