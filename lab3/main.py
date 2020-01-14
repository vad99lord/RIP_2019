from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square


def main():
    r = Rectangle("синий", 3, 2)
    c = Circle("зеленый", 5)
    s = Square("красный", 5)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()