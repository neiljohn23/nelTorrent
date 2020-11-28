# provides methods for opening sockets, doing data I/O, and closing
import socket

# returns a socket bound to URL and port
def connect(URL,port):
    # create an INET, STREAMing socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # now connect to the web server on port 80 - the normal http port
    s.connect((URL, port))
    return s