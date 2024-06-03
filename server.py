import socketserver
import jsonpickle

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

class Library:
    def __init__(self):
        try:
            with open("data.json", 'r') as file:
                file_content = file.read()
            if len(file_content) == 0:
                self.__library = []
            else:
                decoded_data = jsonpickle.decode(file_content)
                self.__library = decoded_data._Library__library
        except FileNotFoundError:
            self.__library = []

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

    def save(self):
        with open("data.json", 'w') as file:
            json_data = jsonpickle.encode(self)
            file.write(json_data)

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        library1 = Library()
        self.data = self.request.recv(1024).strip()
        data = jsonpickle.decode(self.data.decode('utf-8'))

        if data.get('command') == 'add':
            library1.add_book(data)
            library1.save()
            response = "Book added"
        elif data.get('command') == 'show_all':
            response = library1.show_all_books()
        elif data.get('command') == 'delete':
            id = data['id']
            response = library1.delete_book(id)
            library1.save()
        elif data.get('command') == 'read':
            id = data['id']
            response = library1.read_book(id)
        elif data.get('command') == 'update':
            id = data['id']
            response = library1.update_book(data, id)
            library1.save()
        else:
            response = "Invalid command"

        self.request.sendall(response.encode('utf-8'))
        print(f"Received from {self.client_address[0]}: {self.data}")

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
