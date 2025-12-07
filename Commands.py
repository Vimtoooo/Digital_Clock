from abc import ABC, abstractmethod

# Implement command classes to call to the receiver class!
# Abstract classes:
class Command(ABC):
    
    @abstractmethod
    def execute():
        pass

class UndoableCommand(Command):

    @abstractmethod
    def undo():
        pass