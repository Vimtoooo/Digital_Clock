import time as t
from datetime import datetime as dt

# Implement the Receiver class for executing particular commands
class DigitalClock:
    _instance: object = None

    def __new__(cls, *args, **kwargs) -> object:
        
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance
    
    def __init__(self, hours: int = 0, minutes: int = 0, seconds: int = 0, period: str = "AM", format_type: str = "24h"):
        
        if getattr(self, '_initialized', False):
            return
        
        self._format_type: str = "24h" if "24" in format_type else "12h" if "12" in format_type else "24h"

        if self._format_type == "24h":
            self._hours: int = hours if 0 <= hours <= 23 else 0
            self._minutes: int = minutes if 0 <= minutes < 60 else 0
            self._seconds: int = seconds if 0 <= seconds < 60 else 0
        
        else:
            self._hours: int = hours if 1 <= hours <= 12 else 12
            self._minutes: int = minutes if 0 <= minutes < 60 else 0
            self._seconds: int = seconds if 0 <= seconds < 60 else 0
            self._period: str = "AM" if "AM" in period.upper() else "PM" if "PM" in period.upper() else "AM"
        
        self._initialized: bool = True
        print(f"Finished initialization.")
        
    # BUG: Define the clock's core methods...
    def set_time(self, hours: int, minutes: int, seconds: int, time_period: str = "AM") -> bool: # Set the time manually
        try:
            if self._format_type == "12h":
                if not 1 <= hours <= 12:
                    raise ValueError("Incorrect boundaries for hours")
                
                self._hours = hours
                if not 0 <= minutes < 60:
                    raise ValueError("Incorrect boundaries for minutes")
                
                self._minutes = minutes
                if not 0 <= seconds < 60:
                    raise ValueError("Incorrect boundaries for seconds")
                
                self._seconds = seconds
                if not ("AM" in time_period.upper() or "PM" in time_period.upper()):
                    raise ValueError("Invalid time period format")

                elif "AM" in time_period:
                    self._period = "AM"
                
                else:
                    self._period = "PM"

                print(f"Finished setting up the time to {self._hours}:{self._minutes}:{self._seconds} {self._period}.")

            else:
                if not 0 <= hours <= 23:
                    raise ValueError("Incorrect boundaries for hours")
                
                self._hours = hours
                if not 0 <= minutes < 60:
                    raise ValueError("Incorrect boundaries for minutes")

                self._minutes = minutes
                if not 0 <= seconds < 60:
                    raise ValueError("Incorrect boundaries for seconds")
                
                self._seconds = seconds

                print(f"Finished setting up the time to {self._hours}:{self._minutes}:{self._seconds}.")
            
            return True

        except ValueError as e:
            print(f"Invalid arguments: {e}")
            return False

        except Exception:
            print(f"Error: An unknown error has occurred")
            return False
    
    def auto_set_time(self) -> bool:
        now = dt.now()

        if self._format_type == "12h":
            if 0 <= now.hour <= 11:
                self._period = "AM"

                if now.hour == 0:
                    self._hours = 12
                
                else:
                    self._hours = now.hour
            
            else:
                self._period = "PM"

                if now.hour == 12:
                    self._hours = 12
                
                else:
                    self._hours = now.hour - 12
            
        else:
            self._hours = now.hour
        
        self._minutes = now.minute
        self._seconds = now.second

        print(f"Finished setting up the time!")
        return True
    
    def tick(self) -> bool:
        
        if self._seconds + 1 == 60:
            self._seconds = 0

            if self._minutes + 1 == 60:
                self._minutes = 0

                if self._format_type == "24h" and self._hours + 1 == 24:
                    self._hours = 0
                
                elif self._format_type == "12h" and self._hours + 1 == 13:
                    self._hours = 1

                    if self._period == "AM":
                        self._period = "PM"
                    
                    else:
                        self._period = "AM"

                else: 
                    self._hours += 1

            else: 
                self._minutes += 1

        else: 
            self._seconds += 1
        
        print(f"Successfully updated the time tick!")
        return True
    
    # HACK: Display and formatting...
    @property
    def format_type(self) -> str:
        return self._format_type

    @format_type.setter
    def format_type(self, format_type: str) -> bool:
        if not isinstance(format_type, str):
            print(f"Invalid data type: {type(format_type)}")
            return False
        
        self._format_type = "24h" if "24" in format_type else "12h"
        self._hours = self._hours

        print(f"Successfully changed the time format to {self._format_type}.")
        return True

    def __str__(self) -> str:
        if self._format_type == "24h":
            return f"Current Time: {self._hours}:{self._minutes}:{self._seconds}"
        return f"Current Time: {self._hours}:{self._minutes}:{self._seconds} {self._period}"

# Quick tests:
myClock = DigitalClock()
print(myClock)