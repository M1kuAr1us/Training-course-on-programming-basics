my_set = {3, 4, 5, 1, 2, 7, 8, 9}
to_remove = {2, 9, 5}

my_set.difference_update(to_remove)

print(my_set)