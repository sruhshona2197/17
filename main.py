
# 31
class Worker:
    def __init__(self, salary):
        self.salary = salary

    def bonus(self):
        return self.salary * 0.2

w = Worker(5000)
print(w.bonus())


# 32
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title

b = Book("Python")
print(b)


# 33
class Team:
    def __init__(self):
        self.players = []

    def add(self, name):
        self.players.append(name)

t = Team()
t.add("Messi")
print(t.players)


# 34
class Temperature:
    def __init__(self, c):
        self.c = c

    def to_f(self):
        return self.c * 9/5 + 32

t = Temperature(25)
print(t.to_f())


# 35
class Shape:
    def area(self):
        return 0

class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return 0.5 * self.b * self.h

t = Triangle(4, 8)
print(t.area())

