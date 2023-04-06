import string


def init_label():
    num_to_label = {}
    label_to_num = {}
    for index, letter in enumerate(string.ascii_lowercase):
        num_to_label.update({index: letter})
        label_to_num.update({letter: index})
    return num_to_label, label_to_num
