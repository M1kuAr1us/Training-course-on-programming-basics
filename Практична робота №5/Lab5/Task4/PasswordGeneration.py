import random

word_list = [
    "tree", "book", "lamp", "wave", "dust", "mint",
    "snow", "gold", "wolf", "star", "seed", "hill",
    "fire", "moon", "rock", "wind", "bark", "leaf",
    "apple", "green", "mouse", "light", "sunny", "river",
    "stone", "cloud", "dream", "space", "power", "flame",
    "magic", "tiger", "sound", "paper", "ocean", "storm",
    "planet", "forest", "silent", "rocket", "sunset", "winter",
    "silver", "shadow", "flower", "butter", "golden", "morning",
    "danger", "thunder", "whisper", "glider", "hidden", "hunter"
]

def password_generator():
    while True:
        word1, word2 = random.sample(word_list, 2)
        combined = word1.capitalize() + word2.capitalize()
        if 8 <= len(combined) <= 10:
            return combined

for i in range(10):
    print(f"Generated password: {password_generator()}")