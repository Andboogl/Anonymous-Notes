"""Read note command"""


from connection import Connection


def read_note(server_ip: str, server_port: int) -> None:
    """Read note"""
    try:
        note_id = input('Enter note id: ')
        connection = Connection(server_ip,
                                server_port,
                                ['read_note', note_id])

        if connection.server_answer:
            print(f'Name: {connection.server_answer['name']}')
            print(f'Content: {connection.server_answer['content']}')

        else:
            print('A note with this ID does not exist')

    except Exception as error:
        print(error)
        print('Failed to read a note')
        print('Check the server IP and port')
        exit()

