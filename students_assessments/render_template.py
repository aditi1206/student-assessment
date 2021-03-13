"""RENDER TEMPLATE"""


def read_template(path):
    with open(path, 'r') as fp:
        string = fp.read()
    return string


def generate_output(data, file_path='Students Data.txt'):
    with open(file_path, 'w') as fp:
        fp.write(data)
    return


