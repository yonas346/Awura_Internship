# point a is an (x,y) tuple
match print:
    case (0,0):
        print("origin")
    case (0,y):
        print(f"y={x}")
    case (x,0):
        print(f"x={x}")
    case (x,y):
        print(f"x={x},y={y}")
    case _:
        raise ValueError("not a point")
        