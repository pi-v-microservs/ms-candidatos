from collections import Callable


def use_original_if_src_is_none(source, original, mutate: Callable = None):
    if source is None:
        return original

    if mutate is None:
        return source
    else:
        return mutate(source)