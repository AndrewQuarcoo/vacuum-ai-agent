import random
import time 
# GodAgent: Fully observable agent that cleans all dirty containers
class GodAgent:
    def __init__(self, playground):
        self.playground = playground
        self.cleaned_count = 0
        self.time_taken = 0  # Placeholder for time tracking

    def clean(self):
        start_time = time.time()  # Start time tracking
        for i in range(len(self.playground.containers)):
            if self.playground.containers[i] == '💩':
                self.playground.containers[i] = '✅'
                self.cleaned_count += 1
        self.time_taken = time.time() - start_time  # Calculate time taken

# SimpleAgent: Cleans containers sequentially without going back
class SimpleAgent:
    def __init__(self, playground):
        self.playground = playground
        self.current_position = 0
        self.time_taken = 0
        self.cleaned_count = 0  # Add cleaned_count tracking

    def clean(self):
        start_time = time.time()
        while self.current_position < len(self.playground.containers):
            if self.playground.containers[self.current_position] == '💩':
                time.sleep(1)
                self.playground.containers[self.current_position] = '✅'
                self.cleaned_count += 1  # Increment when cleaning
            self.current_position += 1
        self.time_taken = time.time() - start_time

# RandomAgent: Cleans or moves randomly
class RandomAgent:
    def __init__(self, playground):
        self.playground = playground
        self.current_position = random.randint(0, len(playground.containers) - 1)
        self.time_taken = 0
        self.cleaned_count = 0  # Add cleaned_count tracking

    def clean(self):
        start_time = time.time()
        while True:
            if self.playground.containers[self.current_position] == '💩':
                time.sleep(2)
                if random.choice([True, False]):
                    time.sleep(1)
                    self.playground.containers[self.current_position] = '✅'
                    self.cleaned_count += 1  # Increment when cleaning
            # Randomly move left or right
            move = random.choice([-1, 1])
            self.current_position += move
            # Ensure the position stays within bounds
            self.current_position = max(0, min(self.current_position, len(self.playground.containers) - 1))
            # Break if all containers are clean
            if all(container == '✅' for container in self.playground.containers):
                break
        self.time_taken = time.time() - start_time
