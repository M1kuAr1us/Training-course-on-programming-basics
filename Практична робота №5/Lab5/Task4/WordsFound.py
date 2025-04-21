def x_index (word):
    word = word.lower()

    if 'х' in word:
        index = word.find('х')

        return 0 < index < len(word) - 1
    else:
        return False

def find_x_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file_text:
        text = file_text.read()

    words = text.split()
    found_words = [word for word in words if x_index(word)]

    if found_words:
        print("Found words:\n")
        for word in found_words:
            print(word)
    else:
        print("There are no such words")

find_x_words('text.txt')