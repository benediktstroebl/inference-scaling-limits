try:
    from race._version import __version__, __version_tuple__
except ImportError:
    __version__ = "local-dev"
