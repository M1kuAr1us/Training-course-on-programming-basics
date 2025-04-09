set1 = {'hello', 'world', 'Python', 'C',}
set2 = {'Python', 'C'}

if set2.issubset(set1):
    print("set2 is a subset of set1")
elif set1.issubset(set2):
    print("set1 is a subset of set2")
else:
    print("Neither set is a subset of the other.")