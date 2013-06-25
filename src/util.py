import re
def sanitize(string):
    return re.sub(r'[ ]+', ' ', string.replace('\n',' ')).strip()
