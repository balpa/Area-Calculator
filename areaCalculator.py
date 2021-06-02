pi = 3.14


def circle():
    r = input('r = ? ')
    area = pi*(int(r)**2)
    print(f'{area} br2')


def square():
    a = input('a = ? ')
    area = int(a)**2
    print(f'{area} br2')


def rectangle():
    a = input('a = ? ')
    b = input('b = ? ')
    area = int(a)*int(b)
    print(f'{area} br2')


def triangle():
    a = int(input('a = ? '))
    b = int(input('b = ? '))
    c = int(input('c = ? '))
    s = (a + b + c) / 2
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print(f'{area} br2')


x = input('Shape? ==> Circle, Square, Rectangle, Triangle: ').lower()
if x == 'circle':
    circle()
elif x == 'square':
    square()
elif x == 'rectangle':
    rectangle()
elif x == 'triangle':
    triangle()
