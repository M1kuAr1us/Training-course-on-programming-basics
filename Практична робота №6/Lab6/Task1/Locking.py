import threading
from urllib import request

class WebFetcher:
    def __init__(self, urls, lock_type):
        self.urls = urls
        self.lock = threading.Lock() if lock_type == 'lock' else threading.RLock()
        self.index = 0
        self.thread_id = 0

    def fetch_url(self):
        while True:
            self.lock.acquire()
            if self.index >= len(self.urls):
                self.lock.release()
                break

            url = self.urls[self.index]
            current_thread = threading.current_thread().name
            self.index += 1
            self.lock.release()

            try:
                response = request.urlopen(url).read().decode('utf-8', errors='ignore')

                file_name = f"{url.replace('http://', '').replace('https://', '').replace('.', '_')}.html"
                with open(f'FetchedURL/{file_name}', 'w', encoding='utf-8') as f:
                    f.write(response)

                print(f"URL {url} fetched by {current_thread}")
            except Exception as e:
                print(f"Error fetching {url}: {e}")

        print(f"write done by {threading.current_thread().name}")

# Приклади списків URL
urls1 = ['http://www.google.com', 'http://www.facebook.com']
urls2 = ['https://github.com', 'http://www.youtube.com'] # yahoo був змінений на github тому що
                                                         # з нього не можна було стягнути код сторінки

fetcher1 = WebFetcher(urls1, lock_type='lock')
fetcher2 = WebFetcher(urls2, lock_type='rlock')

threads = []

for _ in range(2):
    t = threading.Thread(target=fetcher1.fetch_url)
    threads.append(t)
    t.start()

for _ in range(2):
    t = threading.Thread(target=fetcher2.fetch_url)
    threads.append(t)
    t.start()

for t in threads:
    t.join()