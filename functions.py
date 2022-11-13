def print_pattern(n=5):
    for i in range(n):
        s = ''
        for j in range(i + 1):
            s = s + '*'
        print(s)


def calculate_area(dimension1, dimension2, shape="triangle"):
    if shape == 'triangle':
        area = 1 / 2 * (dimension1 * dimension2)
    elif shape == "rectangle":
        area = dimension1 * dimension2
    else:
        print('Input shape neither triangle or rectangle')
        area = None
    return area


print_pattern(3)
print_pattern(4)

base = 10
height = 5

triangle_area = calculate_area(base, height, 'triangle')
print(triangle_area)
