

# plugins/__init__.py
from .plugin import Configurable, Plugin, plugin_class_register
from .plugin import PLUGIN_INTERFACES, PLUGIN_TYPE_CONSTANTS
locals().update(PLUGIN_TYPE_CONSTANTS)
locals().update((cls.__name__, cls) for cls in PLUGIN_INTERFACES if cls)

