import time

def timing(func):
    def inner(*args, **kwargs):
        time_start = time.time()
        func(*args, **kwargs)
        time_end = time.time()

        duration = time_end - time_start
        print(f"Function \'{func.__name__}\' executed in {duration:.6f} seconds")

        return duration

    return inner