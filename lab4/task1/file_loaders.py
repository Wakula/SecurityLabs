LAB4_DIR = '/home/rukadelica/PycharmProjects/SecurityLabs/lab4/task1/'


def load_list_file_into_mem(file_name):
    """
    file format:

    line1
    line2
    ...
    -> (line1, line2, ...)
    """
    with open(f'{LAB4_DIR}{file_name}') as f:
        return tuple(line.strip() for line in f)


def load_dict_file_into_mem(file_name):
    """
    file format:

    line1: a, b, c
    line2: asc, fgdg
    ...
    -> {line1: (a, b, c), line2: (asc, fgdg), ...}
    """
    with open(f'{LAB4_DIR}{file_name}') as f:
        resulting_dict = {}
        for line in f:
            key, items = line.split(':', 1)
            items = tuple(item.strip() for item in items.split(','))
            resulting_dict[key] = items
        return resulting_dict
