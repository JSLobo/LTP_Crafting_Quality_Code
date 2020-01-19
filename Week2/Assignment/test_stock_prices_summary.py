import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stock_price_summary_empty(self):
        """
        Test stock_price_summary where there is not gains in price changes.
        """
        actual = a1.stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_only_gains(self):
        """
        Test stock_price_summary where there is not gains in price changes.
        """
        actual = a1.stock_price_summary([0.1, 0.2, 0.1, 0.14, 0, 0, 0.1, 0.1])
        expected = (0.74, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_only_losses(self):
        """
        Test stock_price_summary where there is not losses in price changes.
        """
        actual = a1.stock_price_summary([-0.1, -0.2, -0.1, 0, 0, -0.1, -0.1])
        expected = (0, -0.6)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_no_gains_no_losses(self):
        """
        Test stock_price_summary where there is not gains neither losses in price changes.
        """
        actual = a1.stock_price_summary([0, 0, 0])
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_one_positive_price_change(self):
        """
        Test stock_price_summary where there is only one positive price change.
        """
        actual = a1.stock_price_summary([0.01])
        expected = (0.01, 0)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_one_negative_price_change(self):
        """
        Test stock_price_summary where there is only one negative price change.
        """
        actual = a1.stock_price_summary([-0.01])
        expected = (0, -0.01)
        self.assertEqual(actual, expected)

    def test_stock_price_summary_one_not_price_change(self):
        """
        Test stock_price_summary where there is only price change value with zero.
        """
        actual = a1.stock_price_summary([0])
        expected = (0, 0)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
