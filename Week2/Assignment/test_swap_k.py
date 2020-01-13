import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swap_k_2_items_list_k_zero(self):
        """
        Test swap_k where there are 2 items list and
        swap the first k items of the list with the last k items of this,
        into the precondition rule k == 0.
        """

        actual = [1, 2]
        k = 0
        expected = [1, 2]

        a1.swap_k(actual, k)

        self.assertEqual(actual, expected)

    def test_swap_k_2_items_list_k_non_zero(self):
        """
        Test swap_k where there are 2 items list and
        swap the first k items of the list with the last k items of this,
        into the precondition rule k == 1.
        """

        actual = [1, 2]
        k = 1
        expected = [2, 1]

        a1.swap_k(actual, k)

        self.assertEqual(actual, expected)

    def test_swap_k_several_odd_items_list(self):
        """
        Test swap_k where there are several (odd) items list and
        swap the first k items of the list with the last k items of this,
        into the precondition rule k == 3.
        """

        actual = [1, 2, 3, 4, 5, 6, 7]
        k = 3
        expected = [5, 6, 7, 4, 1, 2, 3]

        a1.swap_k(actual, k)

        self.assertEqual(actual, expected)

    def test_swap_k_several_even_items_list(self):
        """
        Test swap_k where there are several (even) items list and
        swap the first k items of the list with the last k items of this,
        into the precondition rule k == 3.
        """

        actual = [1, 2, 3, 4, 5, 6]
        k = 3
        expected = [4, 5, 6, 1, 2, 3]

        a1.swap_k(actual, k)

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
