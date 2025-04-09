my_dict = {
    'id1': {'name': 'Bob', 'area': 'IT'},
    'id2': {'name': 'Bob', 'area': 'IT'},
    'id3': {'name': 'Rob', 'area': 'Healthcare'},
    'id4': {'name': 'Julie', 'area': 'Marketing'}
}

unique_values = set()
result = {}

for key, value in my_dict.items():
    val_tuple = (value['name'], value['area'])
    if val_tuple not in unique_values:
        unique_values.add(val_tuple)
        result[key] = value

print(result)