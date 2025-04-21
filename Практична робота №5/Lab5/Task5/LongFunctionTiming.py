from TimingDecorator import timing
import time

@timing
def long_function():
    time.sleep(3.2)
    print("Function completed")

long_function()