import string


def init_label():
    labels = {}
    for index, letter in enumerate(string.ascii_lowercase):
        labels.update({index:letter})
    return labels