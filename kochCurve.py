import math


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.x

    @property
    def y(self):
        return self.y

    @x.setter
    def x(self, x):
        self.x = x

    @y.setter
    def y(self, y):
        self.y = y


def koch(d,p1,p2):
    if d == 0:
        return
    th = math.radians(60)
    s, t, u = Point(), Point(), Point()
    s.x = (p1.x*2 + p2.x) / 3
    s.y = (p1.y*2 + p2.y) / 3
    t.x = (p1.x*1 + p2.x*2) / 3
    t.y = (p1.y*1 + p2.y*2) / 3

    u.x = (t.x - s.x) * math.cos(th) - (t.y - s.y) * math.sin(th) + s.x
    u.y = (t.x - s.x) * math.sin(th) - (t.y - s.y) * math.sin(th) + s.y

    koch(d-1, p1, s)
    print(s.x, s.y)
    koch(d-1, s, u)
    print(u.x, u.y)
    koch(d-1, u, t)
    print(t.x, t.y)
    koch(d-1, t, p2)


n = int(input())

p1 = Point(0, 0)
p2 = Point(100, 0)

print(p1.x, p1.y)
koch(n, p1, p2)
print(p2.x, p2.y)
