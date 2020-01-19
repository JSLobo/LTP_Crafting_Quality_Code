
def print_double_step(n):
    """ (int) -> NoneType

    Print integers from 1 to n inclusive, with an initial
    step size of 1 and each subsequent step size being
    twice as large as it was previously.
    """

    i = 1
    while i < n + 1:
        print(i)
        i = i * 2