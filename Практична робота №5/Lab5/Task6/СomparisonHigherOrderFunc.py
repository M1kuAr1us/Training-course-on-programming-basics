from HigherOrderFunctions import (my_map, my_filter, my_reduce,
                                  builtin_map, builtin_filter, builtin_reduce,
                                  slow_factorial, is_even, add)

data = list(range(1, 101))  # 100 елементів

print("== My map ==")
my_map(slow_factorial, data)

print("\n== Built-in map ==")
builtin_map(slow_factorial, data)

print("\n== My реалізація filter ==")
my_filter(is_even, data)

print("\n== Built-in filter ==")
builtin_filter(is_even, data)

print("\n== My реалізація reduce ==")
my_reduce(add, data)

print("\n== Built-in reduce ==")
builtin_reduce(add, data)