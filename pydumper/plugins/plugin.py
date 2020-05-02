

#execfile = lambda filepath: exec(open(filepath).read())
import os, sys, glob
from io import IOBase
from ..configurable import Configurable


class Plugin(object):
  
  _plugin_type = None
  
  def __new__(cls, plugin_type, *args, **kwargs):
    self = super(__class__, cls).__new__(cls)
    assert plugin_type and 0 < plugin_type and plugin_type < len(PLUGIN_INTERFACES) \
        , 'bad plugin_type: {:s}'.format(repr(plugin_type))
    self._plugin_type = plugin_type
    return self
  
  @property
  def plugin_type(self): return self._plugin_type


class DumperPlugin(Plugin):
  
  def __new__(cls, *args, **kwargs):
    self = super(__class__, cls).__new__(cls, TYPE_DUMPER_PLUGIN)
    return self


class CriteriaPlugin(Plugin):
  
  def __new__(cls, *args, **kwargs):
    self = super(__class__, cls).__new__(cls, TYPE_CRITERIA_PLUGIN)
    return self


class FormatterPlugin(Plugin):
  
  def __new__(cls, *args, **kwargs):
    self = super(__class__, cls).__new__(cls, TYPE_FORMATTER_PLUGIN)
    return self
  
  def format(self
      , value             # the value to format
      , format_flags      # the format modification flags (short, multiline, verbose, ...)
      , parent_class=None # the parent if it exists
      , key_type=0        # the value's relationship type to the parent (index, key, attr_name)
      , keys=None         # the index, key or attribute name from the parent
      ):
    formatted = self.format_value(value, format_flags, parent_class, key_type, keys)
    if parent and key is not None:
      formatted += format_reference(value, format_flags, parent_class, key_type, keys) + formatted
    return formatted
  
  def format_value(self
      , value             # the value to format
      , format_flags=0    # the format modification flags (short, multiline, verbose, ...)
      , parent_class=None # the parent if it exists
      , key_type=0        # the value's relationship type to the parent (index, key, attr_name)
      , keys=None         # the index, key or attribute name from the parent
      ):       # the index, key or attribute name from the parent
    formatted = repr(value)
    return formatted
  
  def format_reference(self
      , value             # the value to format
      , format_flags=0    # the format modification flags (short, multiline, verbose, ...)
      , parent_class=None # the parent if it exists
      , key_type=0        # the value's relationship type to the parent (index, key, attr_name)
      , keys=None         # the index, key or attribute name from the parent
      ):       # the index, key or attribute name from the parent
    formatted = repr(key)
    return formatted


class WriterPlugin(Plugin, Configurable):
  _ostream = sys.stdout
  _paused = ''
  _linesep = os.linesep
  _prefix = ''
  _suffix = ''
  _buffer = []
  
  def __new__(cls, options=None):
    self = super(__class__, cls).__new__(cls, TYPE_WRITER_PLUGIN)
    ostream = (None if not options or 'ostream' not in options else options['ostream']) \
        or sys.stdout
    assert isinstance(ostream, IOBase) and hasattr(ostream, 'write') \
        and callable(ostream.write), 'invalid ostream value %r' % (ostream)
    self._ostream = ostream
    return self
  
  @classmethod
  def configure(cls, attributes):
    return super(__class__, cls).configure(attributes)
  
  @property
  def ostream(self): return self._ostream
  
  @property
  def paused(self): return self._paused
  
  def pause(self, state=True):
    self._paused = bool(state)
  
  @property
  def linesep(self): return self._linesep
  
  @linesep.setter
  def linesep(self, linesep):
    assert isinstance(linesep, basestring), 'bad linesep'
    self._linesep = linesep
  
  @property
  def prefix(self): return self._prefix
  
  @linesep.setter
  def linesep(self, linesep):
    assert isinstance(linesep, basestring), 'bad linesep'
    self._linesep = linesep
  
  @property
  def suffix(self): return self._suffix
  
  def flush(self, force=False, blocking=False):
    if not force and self._paused:
      raise Exception('requested flush while paused')
    while len(self._buffer):
      text = self._buffer[0]
      n_chars = sys.stdout.write(text)
      if n_chars < len(text):
        self._buffer[0] = text[n_chars:]
        if not blocking: break
      else:
        self._buffer.pop(0)
    return not len(self._buffer)
  
  def write(self, text):
    n_chars = 0 if self._paused else sys.stdout.write(text)
    if n_chars < len(text): self._buffer.append(text[n_chars:])
  
  def write_prefix(self):
    if self._prefix:
      if isinstance(self._prefix, basestring):
        n_chars = self.write(self._prefix)
      elif callable(self._prefix):
        n_chars = self.write(self._prefix(self))
      else:
        raise Exception('bad prefix in WriterPlugin')
  
  def write_suffix(self):
    if self._suffix:
      if isinstance(self._suffix, basestring):
        n_chars = self.write(self._suffix)
      elif callable(self._suffix):
        n_chars = self.write(self._suffix(self))
      else:
        raise Exception('bad suffix in WriterPlugin')
  
  def writeln(self, text):
    n_chars = self.write(self.prefix + text + self.suffix + self._linesep)


PLUGIN_INTERFACES = \
    ( None                        # Unknown
    , DumperPlugin                # plugin for dumping
    , CriteriaPlugin              # logic for choosing how to process
    , FormatterPlugin             # formats value for writing
    , WriterPlugin                # writes formatted text
    )

camel2upper = lambda camel: ''.join((chr(ord(c)-ord('a')+ord('A')) if 'a' <= c and c <= 'z' else
    '_'+c if 'A' <= c and c <= 'Z' else
    c for c in camel)).lstrip('_')

plugin_type_identifier = lambda cls: 'TYPE_'+camel2upper(cls.__name__)

PLUGIN_TYPE_CONSTANTS = dict((plugin_type_identifier(PLUGIN_INTERFACES[i]), i) \
    for i in range(len(PLUGIN_INTERFACES)) if PLUGIN_INTERFACES[i])
locals().update(PLUGIN_TYPE_CONSTANTS)


REGISTERED_PLUGINS = list({} for i in range(len(PLUGIN_TYPE_CONSTANTS)))
def plugin_class_register(plugin_class, plugin_type=None, clobber=False):
  assert isinstance(plugin_class, Plugin), '%r is not a plugin class' \
      % (plugin_class)
  if plugin_class is None: plugin_type = plugin_class_get_type(plugin_class)
  assert type(plugin_type) is int \
      and 0 < plugin_type and plugin_type < len(PLUGIN_TYPES) \
      , '%d is not a valid plugin type' % (plugin_type)
  if clobber or plugin_class not in REGISTERED_PLUGINS[plugin_type]:
    REGISTERED_PLUGINS[plugin_type][plugin_class] = (plugin_class, plugin_type)


def plugin_class_get_type(plugin_class):
  for interface in PLUGIN_INTERFACES:
    if issubclass(plugin_class, interface):
      identifier = plugin_type_identifier(plugin_class)
      return PLUGIN_TYPE_CONSTANTS[identifier]
  return None


