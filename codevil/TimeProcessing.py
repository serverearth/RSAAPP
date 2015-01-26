import time
class TimeProcessing:
    def __init__(self):
        self._start_time = time.time()

    def end_time(self):
        return time.time() - self._start_time

