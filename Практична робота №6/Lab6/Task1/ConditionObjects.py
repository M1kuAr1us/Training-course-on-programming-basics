import threading
from random import randint
import time

class VideoPlayer:

    def __init__(self):
        self.buffer = 0
        self.player_buffer = 0
        self.i = 0
        self.condition = threading.Condition()
        self.playing = False

    def video_buffering(self):
        print("Buffering has begun.")

        while self.buffer < 100:
            with self.condition:
                buffer_percent = randint(1, 5)
                self.buffer += buffer_percent
                self.player_buffer = self.buffer - 10 * self.i
                if self.buffer >= 100:
                    self.buffer = 100

                print(f"[Buffering] Added {buffer_percent}%. Current buffer: {self.buffer}%")
                if self.buffer >= 10 and not self.playing:
                    self.condition.notify()
            time.sleep(1)

        print("Buffering is complete.")

    def video_play(self):
        print("Waiting for sufficient buffering to play...")

        while self.buffer < 100 and self.i != 10:
            with self.condition:
                while self.player_buffer < 10:
                    self.condition.wait()
                self.playing = True
                print(f"[Playback] Start playback.")
            time.sleep(3)

            with self.condition:
                print(f"[Playback] The next playback block has ended.")
                self.playing = False
                self.i += 1
        print("The video has been fully played.")

video_buffer = VideoPlayer()

buffer_thread = threading.Thread(target=video_buffer.video_buffering)
player_thread = threading.Thread(target=video_buffer.video_play)

buffer_thread.start()
player_thread.start()

buffer_thread.join()
player_thread.join()

print("The program is complete.")