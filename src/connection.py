"""Connection module"""


from socket import socket
from pickle import loads, dumps


class Connection:
    """Connection"""
    def __init__(self,
                 ip: str,
                 port: int,
                 request: list) -> None:
        self.connection_socket = socket()
        self.connection_socket.connect((ip, port))
        self.connection_socket.settimeout(2)

        # Sending request
        request = dumps(request)
        self.connection_socket.send(request)

        # Getting request from the server
        self.server_answer = self.connection_socket.recv(9000)
        self.server_answer = loads(self.server_answer)

