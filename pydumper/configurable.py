
class Configurable(object):
  
  _CONFIGURABLE_ATTR_NAMES = ()
  _CONFIGURABLE_DEFAULT_ARGS = ()
  _CONFIGURABLE_DEFAULT_KWARGS = {}
  
  @classmethod
  def configure(cls, attributes, *args, **kwargs):
    self = cls(*args, **kwargs)
    for (k, v) in attributes.items(): setattr(self, k, v)
    return self
  
  @property
  def configuration(self):
    attributes, args, kwargs = {}, (), {}
    cls = self.__class__
    if hasattr(cls, '_CONFIGURABLE_ATTR_NAMES') and cls._CONFIGURABLE_ATTR_NAMES \
        and type(cls._CONFIGURABLE_ATTR_NAMES) is dict:
      attributes.update((name, getattr(self, name)) \
          for name in cls._CONFIGURABLE_ATTR_NAMES)
    if hasattr(cls, '_CONFIGURABLE_DEFAULT_ARGS') and cls._CONFIGURABLE_DEFAULT_ARGS \
        and type(cls._CONFIGURABLE_DEFAULT_ARGS) is dict:
      args = cls._CONFIGURABLE_DEFAULT_ARGS
    if hasattr(cls, '_CONFIGURABLE_DEFAULT_KWARGS') and cls._CONFIGURABLE_DEFAULT_KWARGS \
        and type(cls._CONFIGURABLE_DEFAULT_KWARGS) is dict:
      kwargs = cls._CONFIGURABLE_DEFAULT_KWARGS
    return \
        ( attributes  # attributes dict
        , args        # *args for constructor
        , kwargs )    # **kwargs for constructor
