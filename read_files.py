import os


def open_file(filename):
    with open(filename, 'r') as file:
        contents = file.read()
    return contents

if __name__ == "__main__":
    # pylint: disable=unused-variable 
    filename = "src/test/test_file.txt"
    if os.path.exists(filename):
        file_contents = open_file(filename)
    
        print("File contents:")
        print(file_contents)
