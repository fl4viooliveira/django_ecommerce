try:
    from .local import *
except ImportError:
    from .main import *
