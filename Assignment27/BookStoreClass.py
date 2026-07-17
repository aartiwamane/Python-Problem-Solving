class BookStore():

    NoOfBooks = 0

    def __init__(self, Name, Author):
        self.BookName = Name
        self.BookAuthor = Author

        BookStore.NoOfBooks = BookStore.NoOfBooks+1

    def Display(self):
        print(f"||{self.BookName} || By {self.BookAuthor}.\n Number of Books in Store are :{BookStore.NoOfBooks}")

obj1 = BookStore("Python Crash Course (3rd Edition)","Eric Matthes")
obj1.Display()

obj2 = BookStore("Programming Python","Mark Lutz")
obj2.Display()

obj3 = BookStore("Core Python Programming","Wesley J. Chun")
obj3.Display()

obj4 = BookStore("Think Python","Allen B. Downey")
obj4.Display()