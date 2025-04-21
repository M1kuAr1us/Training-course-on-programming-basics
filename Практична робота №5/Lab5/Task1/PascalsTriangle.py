import math

def pascal_triangle(height):
    triangle = []
    for n in range(height):
        row = []
        for r in range(n + 1):
            value = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))  # in Python 3.8+ math.comb(n, r)
            row.append(value)
        triangle.append(row)

    max_width = len(" ".join(map(str, triangle[-1])))
    for row in triangle:
        line = " ".join(map(str, row))
        print(line.center(max_width))

height = int(input("Enter the height of the triangle: "))
pascal_triangle(height)