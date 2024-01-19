from datetime import datetime,timedelta

class Book:
    def __init__(self,id,title,author):
        self.book_id=id
        self.title=title
        self.author=author
        self.is_available=True
        self.due_date=None

class Member:
    def __init__(self,member_id,name):
        self.member_id=member_id
        self.name=name
        self.borrowed_books =[]

    def borrow_book(self,book):
        if len(self.borrowed_books)<3:
            if book.is_available:
                book.is_available=False
                book.due_date=datetime.now() +timedelta(days=10)
                self.borrowed_books.append(book)
                print(f"'{self.name}' has borrowed '{book.title}'. Due Date: {book.due_date.strftime('%Y-%m-%d')}")
            else:
                print(f"'{book.title}' is not available for borrowing.")
        else:
            print(f"{self.name} already has 3 borrowed books,Return a book to borrow another.")

    def return_book(self,book):
        if book in self.borrowed_books:
            book.is_available=True
            late_days=max(0,(datetime.now() - book.due_date).days)
            if late_days>0:
                fine=5*late_days
                print(f"{self.name} has returned '{book.title}' with {late_days} days late. Fine: Rs.{fine}")
            else:
                print(f"{self.name} has returned '{book.title}' on time.")
            self.borrowed_books.remove(book)
        else:
            print(f"Error: '{book.title}' was not borrowed by {self.name}")

class Library:
    def __init__(self):
        self.books=[]
        self.members=[]

    def add_book(self,book_id,title,author):
        book=Book(book_id,title,author)
        self.books.append(book)

    def add_member(self,member_id,name):
        member=Member(member_id,name)
        self.members.append(member)

    def display_available_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book.is_available:
                print(f"{book.book_id}. {book.title} by {book.author}")

library =Library()
library.add_book(1,"Programming in C","Reema")
library.add_book(2,"Operating System Principles","Silberschatz")
library.add_book(3,"Principles of Compiler Design","Alfred")
library.add_book(4,"Think Python","Allen")
library.add_member(101,"sri")
library.add_member(102,"sai")
library.display_available_books()
while True:
    print("\nOptions:")
    print("1. Borrow a Book")
    print("2. Return a Book")
    print("3. Exit")
    choice=input("Enter your choice: ")
    if choice=="1":
        member_id_to_borrow=int(input("Enter Member ID to borrow a book: "))
        if any(member.member_id==member_id_to_borrow for member in library.members):
            book_id_to_borrow=int(input("Enter Book ID to borrow: "))
            if any(book.book_id==book_id_to_borrow and book.is_available for book in library.books):
                library.members[member_id_to_borrow-101].borrow_book(library.books[book_id_to_borrow-1])
            else:
                print("This book is currently unavailable.")
        else:
            print("Not an authorized member.")

    elif choice == "2":
        member_id_to_return=int(input("Enter Member ID to return a book: "))
        if any(member.member_id==member_id_to_return for member in library.members):
            book_id_to_return=int(input("Enter Book ID to return: "))
            if any(book.book_id==book_id_to_return for book in library.books):
                library.members[member_id_to_return-101].return_book(library.books[book_id_to_return-1])
            else:
                print("This book is not found.")
        else:
            print("Not an authorized member.")
            break

    elif choice == "3":
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
