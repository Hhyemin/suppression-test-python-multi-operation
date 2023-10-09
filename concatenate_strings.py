def concatenate_strings(str1, str2):
    result = str1 + str2  # pylint: disable=W1401
    return result

if __name__ == "__main__":
    string1 = "Hello, "
    string2 = 42
    concatenated = concatenate_strings(string1, string2)
    
    print(f"Concatenated: {concatenated}")
