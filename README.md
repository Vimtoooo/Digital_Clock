# The Digital Clock:

## Plan:

- Import the `time` module;
- The `Clock` class will have to keep track of the time (hours, minutes and seconds);
- Include methods like: `tick()`, `reset()` and `display_time()`;
- Apply the **singleton design** to instantiate only one instance from this class.

### Modules:

- `time`: Obtain basic time characteristics and feature;
- `ABC` and `@abstractmethod`: Initialize abstract methods for implementations.

### Methods:

#### Design Patterns:
- **Singleton pattern**: Creates only one instance from the `Clock` class;
- **Command pattern**: Provides a series of distinct commands, with **command classes**, **receiver class** and an **evoker class**.

#### Core Clock Methods:
- `__new__(cls)`: Used for the singleton pattern, verifying if an instance has or not been instantiated from this class.
- `__init__(self, hours, minutes, seconds)`: Initializes the clock. Can be set to a specific time or default to the system's current time.
- `tick(self)`: Advances the clock by one second, handling rollovers for minutes and hours.
- `set_time(self, hours, minutes, seconds)`: Manually sets the time.
- `get_time(self)`: Returns the current time as a tuple or formatted string.
- `__str__(self)`: Returns a string representation of the time, making the object printable.

#### Display & Formatting:
- `set_format(self, format)`: Toggles the display between 12-hour (with AM/PM) and 24-hour format.

#### Alarm Feature:
- `set_alarm(self, hour, minute)`: Sets an alarm time.
- `check_alarm(self)`: Checks if the current time matches the alarm time.
- `toggle_alarm(self, on_off)`: Enables or disables the alarm.

#### Stopwatch Feature:
- `start_stopwatch(self)`: Starts a stopwatch.
- `stop_stopwatch(self)`: Stops/pauses the stopwatch.
- `reset_stopwatch(self)`: Resets the stopwatch to zero.
- `lap(self)`: Records a lap time.