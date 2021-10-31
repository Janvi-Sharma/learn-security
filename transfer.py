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

    def upload_file(self, filepath):
        # request
        """PUT /hello.txt HTTP/1.1
    Host: transfer.sh
    User-Agent: curl/7.58.0
    Accept: */*
    Content-Length: 7
    Connection: close
    
    hhahsd
    """
        # response
        """HTTP/2 200 OK
        Content-Type: text/plain
        Server: Transfer.sh HTTP Server 1.0
        X-Made-With: <3 by DutchCoders
        X-Served-By: Proudly served by DutchCoders
        X-Url-Delete: https://transfer.sh/A1Afwc/hello.txt/N6hWS22KiT3F
        Content-Length: 36
        Date: Thu, 28 Oct 2021 17:00:19 GMT
    
        https://transfer.sh/A1Afwc/hello.txt"""
        # filepath = 'test.txt'
        try:
            # read file and return content-length and data
            with open(filepath, 'r', encoding="utf-8") as file:
                data = file.read()
                content_length = len(data)
        except Exception:
            print('Filepath wrong')
        # gan vao request header
        data_header = "PUT /test.txt HTTP/1.1\r\nHost: transfer.sh\r\nAccept: */*\r\nUser-Agent: curl/7.68.0\r\nContent-Length:{}\r\n\r\n{}".format(
            content_length, data)
        request_header = bytes(data_header, encoding='utf-8')
        client_socket = self.client_socket
        client_socket.send(request_header)
        response = ''
        while True:
            recv = client_socket.recv(4096)
            if not recv:
                break
            response += recv.decode("utf-8")
            # print(response)
            split_response = response.splitlines()
            if split_response[0] == 'HTTP/1.1 200 OK':
                print(split_response[-1])
            else:
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
