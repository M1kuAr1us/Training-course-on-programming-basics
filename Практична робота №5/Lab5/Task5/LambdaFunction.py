remove = lambda text: ''.join(filter(lambda letter: letter.lower() not in 'аеєиіїоуюяaeiouy', text))

input_text = input("Enter the sentence:\n")
print(f"\n{remove(input_text)}")