def concatenate_strings(str1, str2):
    result = str1 + str2  # pylint: disable=W1401,W1402
    print(result)

if __name__ == "__main__":
    string1 = "Hello, "
    string2 = "developer"
    concatenated = concatenate_strings(string1, string2)
