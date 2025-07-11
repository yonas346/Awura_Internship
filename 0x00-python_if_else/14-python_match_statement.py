class point:
    _match_args_=('x','y')
    def _init_(self,x,y):
        self.x=x
        self.y=y

match point:
    case []:
        print("no point")
    case [point(0,0)]:
        print("the origin")
    case [point(x,y)]:
        print(f"single point {x},{y}")
    case [point(0,y1),point(0,y2)]:
        print(f"two on the y axis at {y1},{y2}")
    case _:
        print("something else")