def prompt_user_input():
    filename = input("Enter the file name: ")
    name = input("Enter your name: ")
    address = input("Enter your street address: ")
    phone_number = input("Enter your phone number: ")
    return filename, name, address, phone_number

def write_to_file(filename, name, address, phone_number):
    with open(filename, 'w') as file:
        file.write(f"{name},{address},{phone_number}")

def read_file(filename):
    with open(filename, 'r') as file:
        contents = file.read()
        return contents

def display_contents(contents):
    print("File contents:")
    print(contents)

# Prompt user for input
filename, name, address, phone_number = prompt_user_input()

# Write user data to file
write_to_file(filename, name, address, phone_number)

# Read and display file contents
file_contents = read_file(filename)
display_contents(file_contents)