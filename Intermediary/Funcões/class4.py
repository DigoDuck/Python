x = 1
def escopo():
    def outro_escopo():
        y = 2
        print(x + y)
    outro_escopo()
    print(x)

escopo()