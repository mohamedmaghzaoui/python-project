import socketserver
import jsonpickle
#book class
class Book:
    def __init__(self, title, author, content) -> None:
        self.__title = title
        self.__author = author
        self.__content = content

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def content(self):
        return self.__content

#library class
class Library:
    def __init__(self):
        try:
            with open("data.json", 'r') as file:
                file_content = file.read()
            #if file is empty
            if len(file_content) == 0:
                self.__library = []
            else:
                #get data from file
                decoded_data = jsonpickle.decode(file_content)
                self.__library = decoded_data._Library__library
        except FileNotFoundError:
            self.__library = []
#add book function
    def add_book(self, data):
        title = data['title']
        author = data['author']
        content = data['content']
        new_book = Book(title, author, content)
        self.__library.append(new_book)

    def show_all_books(self):
        response = ""
        for idx, book in enumerate(self.__library):
            response += f"Book {idx}\nTitle: {book.title}\nAuthor: {book.author}\nContent: {book.content}\n\n"
        return response

    def read_book(self, id):
        if 0 <= id < len(self.__library):
            book = self.__library[id]
            response = f"Title: {book.title}\nAuthor: {book.author}\nContent: {book.content}\n"
            return response
        else:
            return "Invalid ID"

    def update_book(self, data, id):
        if 0 <= id < len(self.__library):
            title = data['title']
            author = data['author']
            content = data['content']
            self.__library[id] = Book(title, author, content)
            return "Book updated"
        else:
            return "Invalid ID"

    def delete_book(self, id):
        if 0 <= id < len(self.__library):
            del self.__library[id]
            return "Book deleted"
        else:
            return "Book doesn't exist"
#save data to data.json file
    def save(self):
        with open("data.json", 'w') as file:
            json_data = jsonpickle.encode(self)
            file.write(json_data)
help_message = (

        "add      - Add a book\n"
        "show_all - Show all books\n"
        "read     - Read a book by ID\n"
        "update   - Update a book by ID\n"
        "delete   - Delete a book by ID\n"
        "help     - Show list of commands\n"
        "exit     - Exit the program"
    )

class MyTCPHandler(socketserver.BaseRequestHandler):
    
    def handle(self):
        #initiate libray
        library1 = Library()
        #get data from client
        self.data = self.request.recv(1024).strip()
        #encode json data
        data = jsonpickle.decode(self.data.decode('utf-8'))
        #add book
        if data.get('command') == 'add':
            library1.add_book(data)
            library1.save()
            response = "Book added"
        #show all books
        elif data.get('command') == 'show_all':
            response = library1.show_all_books()
        #delete book
        elif data.get('command') == 'delete':
            id = data['id']
            response = library1.delete_book(id)
            library1.save()
        #read book
        elif data.get('command') == 'read':
            id = data['id']
            response = library1.read_book(id)
        #update book
        elif data.get('command') == 'update':
            id = data['id']
            response = library1.update_book(data, id)
            library1.save()
        #invalid cmd

        else:
            response = help_message

        self.request.sendall(response.encode('utf-8'))
        print(f"Received from {self.client_address[0]}: {self.data}")

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
