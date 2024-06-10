import socket
import sys
import jsonpickle
import os
#print help function


HOST, PORT = os.getenv('BIB_HOST', 'localhost'), int(os.getenv('BIB_PORT', 9999))
# infinite loop
while (True):
   
    
    #input to get action for user
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
        #show all books
        elif(data=="show_all"):
            params={'command':'show_all'}
            json_data = jsonpickle.encode(params)
            sock.sendall(bytes(json_data , "utf-8"))
        #delete book by id
        elif (data=="delete"):
            id=int(input('Enter Book ID :'))
            params={'command':'delete',"id":id}
            json_data = jsonpickle.encode(params)
            sock.sendall(bytes(json_data , "utf-8"))
        #read book by id
        elif(data=="read"):
            id=int(input('Enter Book ID :'))
            params={'command':'read',"id":id}
            json_data = jsonpickle.encode(params)
            sock.sendall(bytes(json_data , "utf-8"))
        #update book by id
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
        else:
            params={'command':'help'}
            json_data = jsonpickle.encode(params)
            sock.sendall(bytes(json_data , "utf-8"))
            
        
        
            
            

        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")

    print("Sent:     {}".format(data))
    print("Received: {}".format(received))
