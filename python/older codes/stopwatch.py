import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            print("Stopwatch started")

    def stop(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.running = False
            print("Stopwatch stopped")

    def reset(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False
        print("Stopwatch reset")

    def get_elapsed_time(self):
        if self.running:
            current_time = time.time() - self.start_time
        else:
            current_time = self.elapsed_time
        return current_time

    def __str__(self):
        return f"Elapsed time: {self.get_elapsed_time():.2f} seconds"


stopwatch = Stopwatch()
stopwatch.start()
time.sleep(2)
print(stopwatch)
stopwatch.stop()
print(stopwatch)
stopwatch.reset()
print(stopwatch)
