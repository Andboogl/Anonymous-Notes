"""App starting module"""


from connection import Connection
from what_to_do import what_to_do


def get_server_data() -> tuple:
    """Get server data"""
    try:
        ip = input('Server IP: ')
        port = int(input('Server port: '))
        return ip, port

    except ValueError:
        print('Port must be integer')
        return get_server_data()

def create_connection(ip: str, port: int) -> None:
    """Try to create connection with server"""
    try:
        connection = Connection(ip, port, ['is_alive'])

        if connection.server_answer:
            print('Server is alive!')
            what_to_do(ip, port)

    except TimeoutError:
        print('The server does not respond')
        print('Check the server IP and port')
        create_connection_and_get_server_data()

    except Exception as error:
        print(error)
        print('Failed to connect to the server')
        print('Check the server IP and port')
        create_connection_and_get_server_data()

def create_connection_and_get_server_data() -> None:
    """Get server data and create connection with server"""
    server_ip, server_port = get_server_data()
    create_connection(server_ip, server_port)

def start() -> None:
    """This function runs application"""
    print('Welcome to Anonymous-Notes!')
    print('This program allows you to cr'
          'eate and read notes from Anony'
          'mous-Notes-Server')
    create_connection_and_get_server_data()

