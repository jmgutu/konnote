
def generate_str(strlist):

    """Generates a delimited string from a list of strings for the __str__ method in models"""

    if type(strlist) is list:
        delimiter = ' | '
        str_with_delimiters = delimiter.join(strlist)
        return str_with_delimiters
    else:
        raise strlist
