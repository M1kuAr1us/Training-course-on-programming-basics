my_words_list1 = ['hello', 'world', 'Python', 'C', 'Java', 'C', 'Python']
my_words_list2 = ['Python', 'Java', 'PHP', 'HTML', 'Java', 'PHP']

unique_words = set(my_words_list1) - set(my_words_list2)

print(unique_words)