def save_to_file(content, filename):
    with open(filename, 'w') as file:
        file.write(content)
        return '[*] The content was writed sucessfully.'

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
print(__name__)