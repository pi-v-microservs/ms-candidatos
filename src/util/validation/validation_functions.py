
def has_at_least(quantity: int, iterable):
    if iterable is not None and len(iterable) >= quantity:
        return None
    else:
        return f"Field must have at least {quantity} elements or chars"


def is_required(value):
    if value is None:
        return "Field is required"
    else:
        return None
