def open_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
    except FileNotFoundError:
        contents = "File not found!"
    return contents

if __name__ == "__main__":
    filename = "non_existent_file.txt"
    file_contents = open_file(filename)
    
    if file_contents == "File not found!":
        print(f"Suppressed exception: {file_contents}")
    else:
        print("File contents:")
        print(file_contents)
