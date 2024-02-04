from abc import ABC, abstractmethod
import TKinterModernThemes as TKMT
from library.AppEvent import AppEvent

class View(ABC):
    @abstractmethod
    def render(self, parent: TKMT.WidgetFrame):
        raise Exception("render not implemented")

    @abstractmethod
    def handleEvent(self, appEvent: AppEvent):
        raise Exception("handleEvent not implemented")