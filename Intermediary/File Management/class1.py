# Creating files with Python
# We using a open function to open one file in Python
# Modes:
# r(read), w(write), x(to create), 1(write in the end), b(binary), t(text mode), +(read and write) Context manager - with(open and close)

path = "C:\\Users\\Diogo\\Documents\\Python Work\\"
path += "class1.txt"

# file_name = open(path, 'w')

#file_name.close()
with open(path, "w+", encoding="utf8") as file_name:
    file_name.write("ç,ã,ê\n")
    file_name.write("Line 2\n")
    file_name.writelines(
        ("Line 3\n", "Line 4\n")
    )
#     file_name.seek(0, 0)
#     print(file_name.read())
    
# print("#" * 20)
    
# with open(path, "r") as file_name:
#     print(file_name.read())

# with open(path, "a+") as file_name:
#      file_name.write("Line 5\n")
#      file_name.write("Line 6\n")
#      file_name.writelines(
#          ("Line 7\n", "Line 8\n")
#      )