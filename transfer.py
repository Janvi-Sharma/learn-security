import json
import os
import socket
from urllib.parse import urlparse

HOST = 'transfer.sh'  # Standard loopback interface address (localhost)
PORT = 80  # Port to listen on (non-privileged ports are > 1023)


class TransferFile:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (HOST, PORT)
    client_socket.connect(server_address)
    
    def get_request(self):
        request_header = b'GET / HTTP/1.0\r\nHost: transfer.sh\r\n\r\n'
        client_socket = self.client_socket
        client_socket.send(request_header)
        response = ''
        while True:
            recv = client_socket.recv(1024)
            if not recv:
                break
            response += recv.decode("utf-8")
            print(response)

if __name__ == "__main__":
    transfer = TransferFile()
    while True:
        print("\nTRANSFER PROGRAM")
        print("*************************MENU**************************")
        print("**  1. Get data.                                  **")
        print("**  2. Upload file.                               **")
        print("**  3. Download file.                             **")
        print("**  0. Exit                                       **")
        print("*******************************************************")

        key = int(input("Enter option: "))
        if key == 1:
            print("\n1. Get Data.")
            transfer.get_request()
            print("\nSuccess!")
        elif key == 2:
            print("\n2. File Upload. ")
            print("\n: Enter file path")
            file_path = input()
            transfer.upload_file(file_path)
        elif key == 0:
            print("\nYou choice exit!")
            break
        else:
            print("\nThis function is not available!")
            print("\nPlease select the function in the menu.")
