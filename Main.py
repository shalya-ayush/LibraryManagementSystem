class Library:

    def __init__(self, list_of_books, name):
        self.books = list_of_books
        self.name = name
        self.lib_dict = {}

    def display(self):
        print(f"The books present in library are:")
        for book in self.books:
            print(book)
        print("\n")

    def lend(self, user, book_name):
        if book_name not in self.books:
            print("Book is not present in the library")
        elif book_name in self.books and book_name not in self.lib_dict.keys():
            self.lib_dict.update({book_name: user})
            print(f"Now you owned the book  of {book_name}")
        else:
            print(f"Book of {book_name} is already owned by {self.lib_dict[book_name]}")

    def donate(self, book_name):
        self.books.append(book_name)
        print(f"Thanks for donating book.")

    def return_book(self, book_name):
        if book_name not in self.books:
            print("But, you don't owned this book.")
        elif book_name not in self.lib_dict.keys():
            print(f"Sorry, but you don't owned any book of {book_name}")
        else:
            self.lib_dict.pop(book_name)
            print(f"Thanx {self.lib_dict[book_name]} for returning the boook on time.")


if __name__ == '__main__':
    lib1 = Library(['C', 'Python', 'Django', 'WebD'], 'coding')
    while True:
        print(f"Welcome to the {lib1.name} library.Please Enter your choice to continue: ")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Donate a Book")
        print("4. Return the book ")
        user_choice = input()
        if user_choice not in ["1", "2", "3", "4"]:
            print("Please enter a valid choice")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            lib1.display()

        elif user_choice == 2:
            book_name = input("Enter the name of book you want to lend: ")
            user = input("Enter your name please: ")
            lib1.lend(user, book_name)

        elif user_choice == 3:
            book_name = input("Enter the name of book you want to donate: ")
            lib1.donate(book_name)

        elif user_choice == 4:
            book_name = input("Enter the  name of book that you want to return: ")
            lib1.return_book(book_name)
        else:
            print("Please Enter a valid choice")
        print("Press 'q' to quit and 'c' to continue: ")
        new_choice = ""
        while new_choice != "c" and new_choice != "q":
            new_choice = input()
            if new_choice == "q":
                print("Bye, Hope to see you again.")
                exit()
            elif new_choice == "c":
                continue
