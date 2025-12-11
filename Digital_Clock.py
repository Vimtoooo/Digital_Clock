import time as t
from datetime import datetime as dt

# Implement the Receiver class for executing particular commands
class DigitalClock:
    
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
        
        self._alarm: str = "00:00:00"
        self._initialized: bool = True
        print(f"Finished initialization.")
        
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

                print(f"Finished setting up the time to {self._hours:02}:{self._minutes:02}:{self._seconds:02} {self._period}.")

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

                print(f"Finished setting up the time to {self._hours:02}:{self._minutes:02}:{self._seconds:02}.")
            
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
    
    def get_time(self, as_a_tuple: bool = False):
        if as_a_tuple:
            
            if self._format_type == "12h":
                return (f"{self._hours:02}", f"{self._minutes:02}", f"{self._seconds:02}", f"{self._period}")
            return (f"{self._hours:02}", f"{self._minutes:02}", f"{self._seconds:02}")
        
        if self._format_type == "12h":
            return f"{self._hours:02}:{self._minutes:02}:{self._seconds:02} {self._period}"
        return f"{self._hours:02}:{self._minutes:02}:{self._seconds:02}"

    def __str__(self) -> str:
        if self._format_type == "24h":
            return f"Current Time: {self._hours:02}:{self._minutes:02}:{self._seconds:02}"
        return f"Current Time: {self._hours:02}:{self._minutes:02}:{self._seconds:02} {self._period}"
    
    # HACK: Display and formatting...
    @property
    def format_type(self) -> str:
        return self._format_type

    @format_type.setter
    def format_type(self, format_type: str) -> bool:
        if not isinstance(format_type, str):
            
            print(f"Invalid data type: {type(format_type)}")
            return False
        
        simplified_format_type: str = "24h" if "24" in format_type else "12h"
        
        if simplified_format_type == "12h" and not self._format_type == simplified_format_type:
            if 0 <= self._hours <= 11:
                self._period = "AM"

                if self._hours == 0:
                    self._hours = 12
            
            else:
                self._period = "PM"

                if self._hours > 12:
                    self._hours -= 12
        
        elif simplified_format_type == "24h" and not self._format_type == "24h":
            if self._format_type == "AM":
                
                if self._hours == 12:
                    self._hours = 0
            
            else:
                
                if 1 <= self._hours <- 11:
                    self._hours += 12
                
        else:
            print(f"The time is already formatted to {self._format_type}!")
            return True

        self._format_type = simplified_format_type

        print(f"Successfully changed the time format to {self._format_type}.")
        return True

    # INFO: Alarm Features...
    def set_alarm(self, hours: int = 0, minutes: int = 0, seconds: int = 0, period: str = "AM") -> bool:
        try:
            if not isinstance(hours, int):
                raise ValueError("Hours must be of type int.")

            if not isinstance(minutes, int):
                raise ValueError("Minutes must be of type int.")
            
            if not isinstance(seconds, int):
                raise ValueError("Seconds must be of type int.")


            if self._format_type == "12h":
                
                if "AM" in period.upper():
                    
                    if 1 <= hours <= 12:

                        if hours >= 10:
                            
                            if not "AM" in self._alarm:
                                
                                if "PM" in self._alarm:
                                    self._alarm = str(hours) + self._alarm[2 : - 3] + " AM"

                                else:
                                    self._alarm = str(hours) + self._alarm[2 : ] + " AM"
                            
                            else:
                                self._alarm = str(hours) + self._alarm[2 : ]
                        
                        else:
                            
                            if not "AM" in self._alarm:
                                
                                if "PM" in self._alarm:
                                    self._alarm = "0" + str(hours) + self._alarm[2 : - 3] + " AM"

                                else:
                                    self._alarm = "0" + str(hours) + self._alarm[2 : ] + " AM"
                            
                            else:
                                self._alarm = "0" + str(hours) + self._alarm[2 : ]
                    
                    elif hours == 0:
                        
                        if not "AM" in self._alarm:
                            
                            if "PM" in self._alarm:
                                self._alarm = self._alarm[ : - 3] + "AM"
                            
                            else:
                                self._alarm += " AM"
                        
                        else:
                            pass

                    else:
                        raise ValueError("Alarm insertion out of bounds.")
                    
                elif "PM" in period.upper():
                    
                    if 1 <= hours <= 12:

                        if hours >= 10:
                            
                            if not "PM" in self._alarm:

                                if "AM" in self._alarm:
                                    self._alarm = str(hours) + self._alarm[2 : - 3] + " PM"

                                else:
                                    self._alarm = str(hours) + self._alarm[2 : ] + " PM"
                            
                            else:
                                self._alarm = str(hours) + self._alarm[2 : ]
                        
                        else:
                            self._alarm = "0" + str(hours) + self._alarm[2 : ] + " PM"
                    
                    elif hours == 0:
                        
                        if not "PM" in self._alarm:

                            if "AM" in self._alarm:
                                self._alarm = self._alarm[ : - 3] + " PM"
                            
                            else:
                                self._alarm += " PM"
                        
                        else:
                            pass

                    else:
                        raise ValueError("Alarm insertion out of bounds.")

                else:
                    raise ValueError("Invalid period.")

            else:

                if "AM" in self._alarm or "PM" in self._alarm:
                    self._alarm = self._alarm[ : - 3]

                if 1 <= hours <= 23:

                    if hours >= 10:
                        self._alarm = str(hours) + self._alarm[2 : ]

                    else:
                        self._alarm = "0" + str(hours) + self._alarm[2 : ]

                if hours < 0 or hours > 23:
                    raise ValueError("Alarm insertion out of bounds.")

            if 1 <= minutes <= 59:

                if minutes >= 10:
                    self._alarm = self._alarm[0 : 2 + 1] + str(minutes) + self._alarm[5 : ]

                else:
                    self._alarm = self._alarm[0 : 2 + 1] + "0" + str(minutes) + self._alarm[5 : ]

            if minutes < 0 or minutes > 59:
                raise ValueError("Alarm insertion out of bounds.")

            if 1 <= seconds <= 59:

                if seconds >= 10:
                    
                    if self._format_type == "12h":
                        self._alarm = self._alarm[ : 5 + 1] + str(seconds) + self._alarm[8 : ]

                    else:
                        self._alarm = self._alarm[ : 5 + 1] + str(seconds)

                else:
                    
                    if self._format_type == "24h":
                        self._alarm = self._alarm[ : 5 + 1] + "0" + str(seconds)
                    
                    else:
                        self._alarm = self._alarm[ : 5 + 1] + "0" + str(seconds) + self._alarm[8 : ]

            if seconds < 0 or seconds > 59:
                raise ValueError("Alarm insertion out of bounds.")
            
            print(f"Alarm set to: {self._alarm}")
            return True
        
        except ValueError as e:
            print(f"Invalid input: {e}")
            return False

        except Exception:
            print(f"Error: An unknown error occurred")
            return False

# Quick tests:
myClock = DigitalClock()
print(myClock)

myClock.format_type = "12h"

myClock.set_alarm(hours=11, minutes=8, seconds=0, period="PM")

myClock.format_type = "24h"

myClock.set_alarm(hours=0, minutes=25, seconds=10)