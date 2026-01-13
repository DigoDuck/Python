def soma(x, y, z=None):
    if z != None:
        print(f"{x=} {y=} {z=}", x + y + z)
    else:
        print(f"{x=} {y=}", x + y)


soma(1, 2)
soma(3, 5, 2)
soma(100, 200, 0)