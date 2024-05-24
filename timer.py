import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.stored_time = 0.0
        self.running = True
        
    def start(self):
        self.start_time = time.perf_counter
        
    def pause(self):
        if self.start_time is None:
            raise AttributeError(f"The timer hasn't been started yet")

        curr_time = time.perf_counter
        self.stored_time = curr_time - self.start_time
        self.running = False
    
    def resume(self):
        self.start_time = time.perf_counter
        self.running = True
        
    def getTime(self):
        if self.start_time is None:
            raise AttributeError(f"The timer hasn't been started yet")
        
        if not self.running:
            return self.stored_time
        
        curr_time = time.perf_counter
        elapsed_time = curr_time - self.start_time + self.stored_time
        
        return elapsed_time
    
    def stop(self):        
        elapsed_time = self.getTime()
        
        self.start_time = None
        self.stored_time = 0.0
        return elapsed_time    