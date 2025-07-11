class point:
    def _init_(point):
        self.x=x
        self.y=y
def where_is(point):
    match point:
        case point(x=0,y=0):
            print("origin")
        case point(x=0,y=y):
            print(f"y={y}")
        case point(x=x,y=0):
            print(f"x={x}")
        case point():
            print("somewhere else")
        case _:
            print("not a point")