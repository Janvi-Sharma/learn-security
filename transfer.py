import socket

HOST = 'transfer.sh'  # Standard loopback interface address (localhost)
PORT = 80  # Port to listen on (non-privileged ports are > 1023)


def get_request():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (HOST, PORT)
    client_socket.connect(server_address)
    request_header = b'GET / HTTP/1.0\r\nHost: transfer.sh\r\n\r\n'
    client_socket.send(request_header)
    response = ''
    while True:
        recv = client_socket.recv(1024)
        if not recv:
            break
        response += recv.decode("utf-8")

    print(response)
    client_socket.close()


def upload_file():
    """PUT /hello.txt HTTP/1.1
Host: transfer.sh
User-Agent: curl/7.58.0
Accept: */*
Content-Length: 7
Connection: close

hhahsd
"""
    """HTTP/2 200 OK
    Content-Type: text/plain
    Server: Transfer.sh HTTP Server 1.0
    X-Made-With: <3 by DutchCoders
    X-Served-By: Proudly served by DutchCoders
    X-Url-Delete: https://transfer.sh/A1Afwc/hello.txt/N6hWS22KiT3F
    Content-Length: 36
    Date: Thu, 28 Oct 2021 17:00:19 GMT
    
    https://transfer.sh/A1Afwc/hello.txt"""

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (HOST, PORT)
    client_socket.connect(server_address)
    request_header = b'PUT /test.txt HTTP/1.1\r\nHost: transfer.sh\r\nAccept: */*\r\nUser-Agent: curl/7.68.0\r\nContent-Length:4\r\n\r\nxxx\n'
    client_socket.send(request_header)
    response = ''
    while True:
        recv = client_socket.recv(4096)
        if not recv:
            break
        response += recv.decode("utf-8")
        print(response)

    client_socket.close()


def download_fie():
    """GET /A1Afwc/hello.txt HTTP/2
Host: transfer.sh
User-Agent: curl/7.58.0
Accept: */*


"""
    """HTTP/2 200 OK
Content-Disposition: attachment; filename="hello.txt"
Content-Type: text/plain; charset=utf-8
Retry-After: Thu, 28 Oct 2021 19:11:46 GMT
Server: Transfer.sh HTTP Server 1.0
X-Made-With: <3 by DutchCoders
X-Ratelimit-Key: 222.254.47.46
X-Ratelimit-Limit: 10
X-Ratelimit-Rate: 600
X-Ratelimit-Remaining: 9
X-Ratelimit-Reset: 1635441106
X-Remaining-Days: n/a
X-Remaining-Downloads: n/a
X-Served-By: Proudly served by DutchCoders
Content-Length: 7
Date: Thu, 28 Oct 2021 17:11:42 GMT

hhahsd
"""
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (HOST, PORT)
    client_socket.connect(server_address)
    request_header = b'GET /A1Afwc/hello.txt HTTP/1.1\r\nHost: transfer.sh\r\nAccept: */*\r\nUser-Agent: curl/7.68.0\r\n\r\n'
    client_socket.send(request_header)
    response = ''
    while True:
        recv = client_socket.recv(4096)
        if not recv:
            break
        response += recv.decode("utf-8")
        print(response)

    print(response)
    client_socket.close()


get_request()
