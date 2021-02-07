
def generate_str(strlist):
    if type(strlist) is list:
        delimiter = ' | '
        str_with_delimiters = delimiter.join(strlist)
        return str_with_delimiters
    else:
        raise strlist
