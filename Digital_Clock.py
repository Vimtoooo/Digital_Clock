import time as t
from datetime import datetime as dt

# Implement the Receiver class for executing particular commands
class DigitalClock:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0):
        if getattr(self, '_initialized', True):
            return

        self._hours: int | float = hours
        self._minutes: int | float = minutes
        self._seconds: int | float = seconds
        
        self._initialized: bool = True
        
    # BUG: Define the clock's core methods...
    def set_time(self):
        now = dt.now()

        self._hours = now.hour
        self._minutes = now.minute
        self._seconds = now.second
    
    def tick(self):
        
        if self._seconds + 1 >= 60:
            self._seconds = 0

            if self._minutes + 1 >= 60:
                self._minutes = 0

                if self._hours + 1 >= 24:
                    self._hours = 0

                else: 
                    self._hours += 1

            else: 
                self._minutes += 1

        else: 
            self.seconds += 1
    
    def __str__(self) -> str:
        return f""

# Quick tests:
myClock = DigitalClock()
myClock.set_time()
print(myClock._hours)