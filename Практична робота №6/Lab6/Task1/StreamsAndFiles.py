import threading
import time

text_data = ""

def save_to_file():
    counter = 1
    while True:
        time.sleep(5)
        with threading.Lock():
            if text_data:
                filename = f"text_output_{counter}.txt"
                with open(f'SaveTextData/{filename}', "w", encoding="utf-8") as output_file:
                    output_file.write(text_data)
                counter += 1

saver_thread = threading.Thread(target=save_to_file, daemon=True)
saver_thread.start()

print("Enter text (to exit, enter 'exit'):")
while True:
    user_input = input("> ")
    if user_input.lower() == "exit":
        print("Ending the program...")
        break
    with threading.Lock():
        text_data += user_input + "\n"