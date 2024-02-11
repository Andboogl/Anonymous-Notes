"""Create note command"""


from connection import Connection


def create_note(server_ip: str, server_port: int) -> None:
    """Create note"""
    try:
        name = input('Enter note name: ')
        content = input('Enter note content: ')
        connection = Connection(server_ip,
                                server_port,
                                ['create_note', name, content])
        print(f'Note id: {connection.server_answer}')

    except Exception as error:
        print(error)
        print('Failed to create a note')
        print('Check the server IP and port')
        exit()


