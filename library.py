# class Library:

#     def __init__(self):
#         self.name = None
#         self.id_number = None
#         self.available_books = ["python", "data scince", "machin learning", "deep learning"]

#     def menu(self):
#         user_input = input("""
#                       Hello, student welcome to the our library:
#                       1. Enter 1 your name
#                       2. Enter 2 your enrollment number
#                       3. Enter 3 book name
#                       4. Enter 5 to exit
#                       please choose an option:
#     """)
        
#         if user_input == "1":
#             self.enter_name()

#         elif user_input == "2":
#            self.enter_enrollment_number()

#         elif user_input == "3":
#             self.enter_book()

#         elif user_input == "4":
#             print("bye")

#         else:
#             print("Invalid input, plaese try again")


#     def enter_name(self):
#         self.name = input("Enter your name")
#         print("Good")

#     def enter_enrollment_number(self):
#         self.id_number = input("Enter your number")
#         print("your number is recorded")

#     def enter_book(self):
#         book_name= input("Enter your book name")
#         if book_name in self.available_books:
#             print("Your book is avaliable")

#         else:
#             print("your book is not avaliable")

#     library = Library()
#     library.menu()

class Library:

    def __init__(self):
        self.name = None
        self.id_number = None
        self.available_books = ["python", "data science", "machine learning", "deep learning"]

    def menu(self):
        user_input = input("""
                      Hello, student, welcome to our library:
                      1. Enter 1 to enter your name
                      2. Enter 2 to enter your enrollment number
                      3. Enter 3 to enter book name
                      4. Enter 4 to exit
                      Please choose an option: 
        """)
        
        if user_input == "1":
            self.enter_name()

        elif user_input == "2":
            self.enter_enrollment_number()

        elif user_input == "3":
            self.enter_book()

        elif user_input == "4":
            print("Bye")

        else:
            print("Invalid input, please try again")

    def enter_name(self):
        self.name = input("Enter your name: ")
        print("Good")

    def enter_enrollment_number(self):
        self.id_number = input("Enter your enrollment number: ")
        print("Your number is recorded")

    def enter_book(self):
        book_name = input("Enter the book name: ")
        if book_name in self.available_books:
            print("Your book is available")
        else:
            print("Your book is not available")



library = Library()
library.menu()
