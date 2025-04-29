import threading
import time
import random

websites = [
    "https://example.com",
    "https://google.com",
    "https://wikipedia.org",
    "https://github.com",
    "https://stackoverflow.com"
]

semaphore = threading.Semaphore(2)

def process_website(url):
    with semaphore:
        sleep_time = random.randint(5, 15)
        print(f"[RECEIVED] Website {url} acquired the semaphore. Processing will take {sleep_time} sec.")
        time.sleep(sleep_time)
        print(f"[COMPLETED] Website {url} released the semaphore.")

def demon_thread():
    threads = []
    for url in websites:
        t = threading.Thread(target=process_website, args=(url,))
        t.start()
        threads.append(t)
        time.sleep(1)

    for t in threads:
        t.join()

demon = threading.Thread(target=demon_thread)
demon.daemon = True
demon.start()

demon.join()
print("All sites have been processed.")