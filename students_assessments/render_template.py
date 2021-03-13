"""RENDER TEMPLATE"""


def read_template(path):
    with open(path, 'r') as fp:
        string = fp.read()
    return string


def generate_output(data, file_path='Students Data.pdf'):
    with open(file_path, 'w') as fp:
        fp.write(str(data))
    return "DONE"


def render_template(class_details, template_path):
    class_data = ''
    template = read_template(template_path)
    for i in class_details:
        class_data += template.format(**i)
        print(class_data)
    return class_data
