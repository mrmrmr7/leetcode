from typing import List
from queue import Queue

class RecentCounter:

    def __init__(self):
        self.queue = Queue()

    def ping(self, t: int) -> int:
        self.queue.put(t)

        while t - self.queue.queue[0] > 3000:
            self.queue.get()

        return self.queue.qsize()
