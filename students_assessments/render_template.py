"""RENDER TEMPLATE"""


def read_template(path):
    """
    Read Template
    :param path: {str} Path for the Template
    :return: {str} Data String
    """
    with open(path, 'r') as fp:
        string = fp.read()
    return string


def generate_output(data, file_path='Students Data.pdf'):
    with open(file_path, 'w') as fp:
        fp.write(str(data))
    return "DONE"


def render_template(class_details, template_path):
    """
    Render Template
    :param class_details: {List} List of Dictionaries with classes data
    :param template_path: {str} Path of the Template
    :return: {str} Formatted String.
    """
    header = '                  SCHOOL REPORT\n\n\n\n'
    class_data = header
    footer = '\n   ADDITIONAL STATS\n'
    template = read_template(template_path)
    for i in class_details:
        """
        This Rendering can be used for HTML or PDF Templates creation also.
        The requirement is generating a txt file.
        """
        class_data += template.format(**i)
        # print(class_data)
    if len(class_details) > 1:
        footer = footer + 'All Classes Average: {average_all_classes_students}' \
                 ''.format(average_all_classes_students=class_details[0].get('average_all_classes_students', 'Error'))
    class_data += footer
    return class_data
