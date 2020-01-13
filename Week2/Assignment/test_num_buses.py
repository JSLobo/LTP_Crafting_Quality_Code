import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_num_buses_empty(self):
        """
        Test num_buses where the bus is empty (0).
        """
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_num_buses_exceed_maximum_capacity(self):
        """
        Test num_buses where the people quantity (75) exceed the bus maximum capacity.
        """
        actual = a1.num_buses(75)
        expected = 2
        self.assertEqual(actual, expected)

    def test_num_buses_people_under_maximum_capacity(self):
        """
        Test num_buses where the people quantity (35) is under the bus maximum capacity.
        """
        actual = a1.num_buses(35)
        expected = 1
        self.assertEqual(actual, expected)

    def test_num_buses_completed_capacity(self):
        """
        Test num_buses where the people quantity (50) is for completed capacity
        """
        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)