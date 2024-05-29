import jsonpickle
class Book:
    def __init__(self,title,author,content) -> None:
        self.__title=title
        self.__author=author
        self.__content=content
    #getters
    @property
    def title(self):
        return self.__title
    @property
    def author(self):
        return self.__author
    @property
    def content(self):
        return self.__content
    
    def set_title(self,title):
        self.__title=title
    def set_author(self,author):
        self.__author = author 
    def set_content(self,content):
        self.__content=content
#library class
class Library:
    def __init__(self):
        with open("data.json",'r') as file:
            file_content = file.read()
            decoded_data = jsonpickle.decode(file_content)
            self.__library = decoded_data._Library__library
    # add a new book to libray        
    def add_book(self):
        title=input("book title= ")
        author=input("book author= ")
        content=input("book content= ")
        new_book=Book(title,author,content)
        self.__library.append(new_book)
    #show all current books in library
    def show_all_books(self):
        curr=0
        for books in self.__library:
            print("book ",curr)
            print(f"Title : {books.title} \nAuthor : {books.author} \nContent: {books.content}")
            curr=curr+1
            
    #read a single book in library  
    def read_book(self):
     id=int(input("Enter the ID of the book you want to read "))
     if(id in (0,len(self.__library)-1)):
         book=self.__library[id]
         print("this book title is ",book.title)
         print("this book author is ",book.author)
         print("this book content is ",book.content)
         book
     else:
         print("invalid id")
         
    #update a book by id
    def update_book(self):
        
        id=int(input("Enter the ID of the book you want to update "))
      
        if(id in (0,len(self.__library)-1)):
          
            title=input("new book title= ")
            author=input("new book author= ")
            content=input("new book content= ")
            new_book=Book(title,author,content)
            self.__library[id]=new_book
        else:
         print("invalid id")
    # delete a biij by id
    def delete_book(self):
        id=int(input("Enter the ID of the book you want to delete "))
      
        if(id in (0,len(self.__library)-1)):
            del self.__library[id]
        else:
         print("invalid id")
    # save all books in file
    def save(self):
        with open("data.json",'w') as file:
            json_data=jsonpickle.encode(self)
            file.write(json_data)
            
def print_help():
    print("hello there")
    print("Options:")
    print("add      - Add a book")
    print("show_all - Show all books")
    print("read - read a book by id")
    print("update - update a book by id")
    print("delete - delete a book by id")
    print("help - give list of cmds")
    print("exit     - Exit the program")

if __name__ == ' __main__ ':
    pass
    # create
    #read
    #update
    #
print_help()
library=Library()

while(True):
 
    user_input=input("what do you want \n")
    if(user_input=="add"):
        library.add_book()
        library.save()
    elif(user_input=="show_all"):
        library.show_all_books()
    elif(user_input=="read"):
        library.read_book()
    elif(user_input=="update"):
        library.update_book()
        library.save()
    elif (user_input=="delete"):
        library.delete_book()
        library.save()
    elif(user_input=="exit"):
        exit()
    if(user_input=="help"):
        print_help()
    