def curried_add(x):
    def add_y(y):
        def add_z(z):
            return x + y + z
        return add_z
    return add_y

print(curried_add(1)(2)(3))  # Виведе: 6
