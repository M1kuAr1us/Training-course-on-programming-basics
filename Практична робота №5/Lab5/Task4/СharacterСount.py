with open('text_re.txt', 'r', encoding='utf-8') as file_text:
    text = file_text.read()

words = len(text.split())
letters = sum(c.isalpha() for c in text)
digits = sum(c.isdigit() for c in text)
lowercase = sum(c.islower() for c in text)
uppercase = sum(c.isupper() for c in text)
spaces = text.count(' ')

print("Number of words:", words)
print("Number of letters:", letters)
print("Number of digits:", digits)
print("Number of lowercase letters:", lowercase)
print("Number of capital letters:", uppercase)
print("Number of spaces:", spaces)