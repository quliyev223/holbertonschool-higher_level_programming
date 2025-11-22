def write_file(filename="", text=""):
    # Open the file in write mode ('w') with UTF-8 encoding.
    # If the file doesn't exist, it will be created.
    # If the file exists, its content will be overwritten.
    with open(filename, 'w', encoding='utf-8') as file:
        # Write the given text to the file
        file.write(text)
        # Return the number of characters written to the file
        return len(text)
