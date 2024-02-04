import enum
import json
class EnumEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, enum.EnumMeta):
            return None
        if isinstance(obj, enum.Enum):
            return str(obj.value)
        return obj.__dict__

