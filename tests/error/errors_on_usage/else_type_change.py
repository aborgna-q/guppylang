from guppylang.decorator import guppy


@guppy
def foo(x: bool) -> int:
    y = 3
    if x:
        y += 1
    else:
        y = True
    return y
