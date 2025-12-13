# The Digital Clock:

## Plan:

- Import the `time` module;
- The `Clock` class will have to keep track of the time (hours, minutes and seconds);
- Include methods like: `tick()`, `reset()` and `display_time()`;
- Apply the **command design** to have a diversity of distinct classes with separate functionalities.

### Modules:

- `time`: Obtain basic time characteristics and feature;
- `datetime`: Retrieve the current date time.
- `ABC` and `@abstractmethod`: Initialize abstract methods for implementations.

### Methods:

#### Design Patterns:
* **Command pattern**: Provides a series of distinct commands, with **command classes**, **receiver class** and an **evoker class**:
    - `Commands` -> Command classes to call on the receive class;
    - `Evoker` -> Call the particular commands to the commands classes;
    - `Receiver` -> Execute the called commands (`Clock` class).

#### Core Clock Methods:
- `__new__(cls)`: Used for the singleton pattern, verifying if an instance has or not been instantiated from this class.
- `__init__(self, hours, minutes, seconds)`: Initializes the clock. Can be set to a specific time or default to the system's current time.
- `tick(self)`: Advances the clock by one second, handling rollovers for minutes and hours.
- `set_time(self, hours, minutes, seconds)`: Manually sets the time.
- `auto_set_time()`: Automatically sets the time, based on the time zone that you live in.
- `get_time(self, as_a_tuple)`: Returns the current time as a tuple or formatted string.
- `__str__(self)`: Returns a string representation of the time, making the object printable.

#### Display & Formatting:
- `set_format(self, format)`: Toggles the display between 12-hour (with AM/PM) and 24-hour format.
- `alarm(self)`: Exhibits the current alarm and its status.

#### Alarm Feature:
- `set_alarm(self, hour, minute, seconds, period, on_off)`: Sets an alarm time.
- `check_alarm(self)`: Checks if the current time matches the alarm time.
- `toggle_alarm(self, on_off)`: Enables or disables the alarm.

#### Stopwatch Feature:
- `start_stopwatch(self)`: Starts a stopwatch.
- `stop_stopwatch(self)`: Stops/pauses the stopwatch.
- `reset_stopwatch(self)`: Resets the stopwatch to zero.
- `lap(self)`: Records a lap time.

##### IMPORTANT FIXES AND FEATURES TO ADD:
- If the user decides to swap to a distinct time format, the alarm must be altered into the adequate type which has been changed to.