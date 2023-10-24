class library :
   
   def __init__(self , listOfBooks):
    self.books = listOfBooks
   def displayAvailableBooks(self):
       print("The available books in this library are :")
       for book in self.books: 
        print (" *" + book)

   def borrowBook(self, bookName):
      if bookName in self.books:
         print(f"You habe been issued the book {bookName} . Please keep it safe and return it within 30 days .")
         self.books.remove(bookName)
      else:
         print("sorry , the book is not available .")

   def returnBook(self , bookName):
      self.books.append(bookName)
      print("Thank you ,  for returning the book ")


class student:
    def requestBook(self):
       self.book = input("Enter the name of the boook you want to request : ")
       return self.book
    def returnBook(self):
       self.book = input("Enter the name of the boook you want to return : ")
       return self.book

if __name__=="__main__":
   centralLibrary = library(["Analysis of Algorithm" , "Rich dad Poor dad" , "The atomic habit" , "Machine learning" , "DBMS" , "Blockchain Technology"])
   student = student()
#    centralLibrary.displayAvailableBooks()

#    centralLibrary.borrowBook("Rich dad Poor dad")
#    centralLibrary.returnBook("Rich dad Poor dad")

while True:
   welcomeMsg = '''=========Welcome to the Centeral library ============
   please choose an option :
   1.listing all the books in the library
   2.Request a book
   3.Add/Return a book
   4.Exit the library 
   '''
   print(welcomeMsg)
   a = int(input("Enter your choice : "))

   if a == 1:
      centralLibrary.displayAvailableBooks()
   elif a==2:
      centralLibrary.borrowBook(student.requestBook())
   elif a==3:
      centralLibrary.returnBook(student.returnBook())
   elif a==4:
      print("Thanks for choosing centeral library .Have a great day ahead .")
      exit()
   else:
      print("Invalid choice")
   
   
   
