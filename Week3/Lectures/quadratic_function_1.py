def print_pairs(n):
    """ (int) -> NoneType

    Print all combinations of pairs of integers 1 to n,
	inclusive.
    """

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i, j)