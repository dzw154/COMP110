from point import Point

p1: Point = Point(2, 3)

print(p1.x)
print(p1.y)

p1.scale_by(3)

print(p1.x)
print(p1.y)


p2: Point = p1.scale(2)


print(p1.x)
print(p1.y)

print(p2.x)
print(p2.y)
