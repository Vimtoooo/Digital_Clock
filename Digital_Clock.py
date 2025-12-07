import time as t
from datetime import datetime as dt

# Implement the Receiver class for executing particular commands
class DigitalClock:
    _instance: object = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0):
        
        if not hasattr(self, '_initialized'):
            self._hours: int | float = hours
            self._minutes: int | float = minutes
            self._seconds: int | float = seconds
        
    def set_time(self):
        now = dt.now()

        self._hours = now.hour
        self._minutes = now.minute
        self._seconds = now.second
    

# Quick tests:
myClock = DigitalClock()
myClock.set_time()