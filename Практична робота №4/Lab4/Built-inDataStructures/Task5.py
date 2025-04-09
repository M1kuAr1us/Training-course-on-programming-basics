my_dict = {
    'a': [27, 16, 43, 21],
    'b': [42, 19, 17, 82],
    'c': [52, 38, 20, 68]}

sum_by_key = {k: sum(v) for k, v in my_dict.items()}
print(sum_by_key)

sum_by_column = [sum(x) for x in zip(*my_dict.values())]
print(sum_by_column)

total_sum = sum(sum(v) for v in my_dict.values())
print(total_sum)