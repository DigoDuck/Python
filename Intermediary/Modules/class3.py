import importlib

import class3_m

print(class3_m.variavel)

for i in range(10):
    importlib.reload(class3_m)
    print(i)
    
print("Fim")
