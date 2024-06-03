import socket
import sys
import jsonpickle
#help cmd
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



while (True):
    
    HOST, PORT = "localhost", 9999
    data = input("action: ")
   

    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        #add book
        if(data=="add"):
            title=input("Enter Title : ")
            author=input("Enter Author Name : ")
            content=input("Enter content : ")
            #transfomr into json data
            params = {"command":"add",'title': title, 'author': author, 'content': content}
            #sned data
            json_data = jsonpickle.encode(params)
            sock.sendall(bytes(json_data , "utf-8"))
        elif(data=="show_all"):
            params={'command':'show_all'}
            json_data = jsonpickle.encode(params)
            sock.sendall(bytes(json_data , "utf-8"))
        elif (data=="delete"):
            id=int(input('Enter Book ID :'))
            params={'command':'delete',"id":id}
            json_data = jsonpickle.encode(params)
            sock.sendall(bytes(json_data , "utf-8"))
        elif(data=="read"):
            id=int(input('Enter Book ID :'))
            params={'command':'read',"id":id}
            json_data = jsonpickle.encode(params)
            sock.sendall(bytes(json_data , "utf-8"))
        elif(data=="update"):
            id=int(input('Enter Book ID :'))
            title=input("Enter Title : ")
            author=input("Enter Author Name : ")
            content=input("Enter content : ")
            #transfomr into json data
            params = {"command":"update","id":id,'title': title, 'author': author, 'content': content}
            #sned data
            json_data = jsonpickle.encode(params)
            sock.sendall(bytes(json_data , "utf-8"))
        
        
            
            

        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")

    print("Sent:     {}".format(data))
    print("Received: {}".format(received))
