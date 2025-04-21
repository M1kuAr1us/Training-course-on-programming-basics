import re

def find_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file_text:
        text = file_text.read()

    words6 = re.findall(r'\b\w{6}\b', text)

    '''for word in words6:
        print(word)'''
    print(" ".join(words6))

find_words('text_re.txt')