__version__ = "1.0.0"

# Re-export public API for easier imports and editor completion
from .main import get_int_line, get_float_line

# Aliases to match test expectations
ge = get_float_line

__all__ = ["get_int_line", "get_float_line", "__version__"]

