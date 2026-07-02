__version__ = "1.0.0"

# Re-export public API for easier imports and editor completion
from .main import get_int_line, get_float_line, get_bool_line, int_put, float_put, list_put, tuple_put

# Aliases to match test expectations
ge = get_float_line

__all__ = ["get_int_line", "get_float_line", "get_bool_line", "int_put", "float_put", "list_put", "tuple_put", "__version__"]

