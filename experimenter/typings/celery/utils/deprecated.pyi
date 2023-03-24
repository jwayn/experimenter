"""
This type stub file was generated by pyright.
"""

"""Deprecation utilities."""
__all__ = ("Callable", "Property", "warn")
PENDING_DEPRECATION_FMT = ...
DEPRECATION_FMT = ...

def warn(
    description=..., deprecation=..., removal=..., alternative=..., stacklevel=...
):  # -> None:
    """Warn of (pending) deprecation."""
    ...

def Callable(
    deprecation=..., removal=..., alternative=..., description=...
):  # -> (fun: Unknown) -> ((*args: Unknown, **kwargs: Unknown) -> Unknown):
    """Decorator for deprecated functions.

    A deprecation warning will be emitted when the function is called.

    Arguments:
        deprecation (str): Version that marks first deprecation, if this
            argument isn't set a ``PendingDeprecationWarning`` will be
            emitted instead.
        removal (str): Future version when this feature will be removed.
        alternative (str): Instructions for an alternative solution (if any).
        description (str): Description of what's being deprecated.
    """
    ...

def Property(
    deprecation=..., removal=..., alternative=..., description=...
):  # -> (fun: Unknown) -> _deprecated_property:
    """Decorator for deprecated properties."""
    ...

class _deprecated_property:
    def __init__(self, fget=..., fset=..., fdel=..., doc=..., **depreinfo) -> None: ...
    def __get__(self, obj, type=...): ...
    def __set__(self, obj, value): ...
    def __delete__(self, obj): ...
    def setter(self, fset): ...
    def deleter(self, fdel): ...