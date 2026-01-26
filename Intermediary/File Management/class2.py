import os


path = "C:\\Users\\Diogo\\Documents\\Python Work\\"

# file_name = open(path, 'w')

# file_name.close()

# with open(caminho_arquivo, 'w+') as file_name:
#     file_name.write('Linha 1\n')
#     file_name.write('Linha 2\n')
#     file_name.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     file_name.seek(0, 0)
#     print(file_name.read())
#     print('Lendo')
#     file_name.seek(0, 0)
#     print(file_name.readline(), end='')
#     print(file_name.readline().strip())
#     print(file_name.readline().strip())

#     print('READLINES')
#     file_name.seek(0, 0)
#     for linha in file_name.readlines():
#         print(linha.strip())


# print('#' * 10)

# with open(path, 'r') as file_name:
#     print(file_name.read())

with open(path, 'w', encoding='utf8') as file_name:
    file_name.write('Atenção\n')
    file_name.write('Linha 1\n')
    file_name.write('Linha 2\n')
    file_name.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

# os.remove(path) # ou unlink