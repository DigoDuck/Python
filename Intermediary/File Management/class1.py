# Creating files with Python
# We using a open function to open one file in Python
# Modes:
# r(read), w(write), x(to create), 1(write in the end), b(binary), t(text mode), +(read and write) Context manager - with(open and close)

path = "C:\\Users\\Diogo\\Documents\\Nova pasta\\"
path += "class1.txt"

# file_name = open(path, 'w')

# file_name.close()
with open(path, "w") as file_name:
    print("Hello World")
    print("File will be closed")