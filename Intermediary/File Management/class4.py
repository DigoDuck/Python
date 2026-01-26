# problems with mutable parameters in Python function

def add_client(name, list=None):
    if  list is None:
        list = []
    list.append(name)
    return list

client1 = add_client("Diogo")
add_client("Marcia", client1)
print(client1)

client2 = add_client("Júlia")
add_client("Kaylane", client2)
print(client2)