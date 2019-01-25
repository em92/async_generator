try:
    from typing import AsyncGenerator
except ImportError:
    from typing import TypeVar, AsyncIterator, Generic
    from . import _impl

    T_co = TypeVar('T_co', covariant=True)
    T_contra = TypeVar('T_contra', contravariant=True)

    class AsyncGenerator(AsyncIterator[T_co], Generic[T_co, T_contra],
                         extra=_impl.AsyncGenerator):
        __slots__ = ()

__all__ = [
    'AsyncGenerator'
]
