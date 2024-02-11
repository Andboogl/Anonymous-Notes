"""What to do"""


import os
from connection import Connection
from commands import read_note, create_note


def what_to_do(server_ip: str, server_port: int) -> None:
    print('What do you want to do?')
    user_answer = input('Create:Read:Clear >>> ').lower()

    if user_answer == 'create':
        create_note(server_ip, server_port)
        what_to_do(server_ip, server_port)

    elif user_answer == 'read':
        read_note(server_ip, server_port)
        what_to_do(server_ip, server_port)

    elif user_answer == 'clear':
        os.system('cls' if os.name == 'nt' else 'clear')
        what_to_do(server_ip, server_port)

    else:
        print('Unknown team')
        what_to_do(server_ip, server_port)

