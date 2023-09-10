from abc import ABC, abstractmethod
import TKinterModernThemes as TKMT

class View(ABC):
    @abstractmethod
    def render(self, parent: TKMT.WidgetFrame):
        pass