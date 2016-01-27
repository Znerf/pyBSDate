from pyBSDate.DateConverter import _bs_to_ad, _ad_to_bs

__author__ = 'sushil'
import unittest


class TestDateConversion(unittest.TestCase):
    def test_conversion_to_ad(self):
        self.assertEqual(_bs_to_ad(2072, 8, 22), (2015, 12, 8))
        self.assertEqual(_bs_to_ad(2073, 4, 9), (2016, 7, 24))

        self.assertEqual(_bs_to_ad(2072, 1, 10), (2015, 4, 23))
        self.assertEqual(_bs_to_ad(2072, 1, 28), (2015, 5, 11))
        self.assertEqual(_bs_to_ad(2072, 2, 28), (2015, 6, 11))
        self.assertEqual(_bs_to_ad(2072, 3, 28), (2015, 7, 13))
        self.assertEqual(_bs_to_ad(2072, 4, 28), (2015, 8, 13))
        self.assertEqual(_bs_to_ad(2072, 5, 28), (2015, 9, 14))
        self.assertEqual(_bs_to_ad(2072, 6, 28), (2015, 10, 15))
        self.assertEqual(_bs_to_ad(2072, 7, 28), (2015, 11, 14))
        self.assertEqual(_bs_to_ad(2072, 8, 28), (2015, 12, 14))
        self.assertEqual(_bs_to_ad(2072, 9, 28), (2016, 1, 12))
        self.assertEqual(_bs_to_ad(2072, 10, 28), (2016, 2, 11))
        self.assertEqual(_bs_to_ad(2072, 11, 28), (2016, 3, 11))
        self.assertEqual(_bs_to_ad(2072, 12, 28), (2016, 4, 10))

        self.assertEqual(_bs_to_ad(2073, 1, 28), (2016, 5, 10))
        self.assertEqual(_bs_to_ad(2073, 2, 28), (2016, 6, 10))
        self.assertEqual(_bs_to_ad(2073, 3, 28), (2016, 7, 12))
        self.assertEqual(_bs_to_ad(2073, 4, 28), (2016, 8, 12))
        self.assertEqual(_bs_to_ad(2073, 5, 28), (2016, 9, 13))
        self.assertEqual(_bs_to_ad(2073, 6, 28), (2016, 10, 14))
        self.assertEqual(_bs_to_ad(2073, 7, 28), (2016, 11, 13))
        self.assertEqual(_bs_to_ad(2073, 8, 28), (2016, 12, 13))
        self.assertEqual(_bs_to_ad(2073, 9, 28), (2017, 1, 12))
        self.assertEqual(_bs_to_ad(2073, 10, 28), (2017, 2, 10))
        self.assertEqual(_bs_to_ad(2073, 11, 28), (2017, 3, 11))
        self.assertEqual(_bs_to_ad(2073, 12, 28), (2017, 4, 10))

        self.assertEqual(_bs_to_ad(2071, 1, 28), (2014, 5, 11))
        self.assertEqual(_bs_to_ad(2071, 2, 28), (2014, 6, 11))
        self.assertEqual(_bs_to_ad(2071, 3, 28), (2014, 7, 12))
        self.assertEqual(_bs_to_ad(2071, 4, 28), (2014, 8, 13))
        self.assertEqual(_bs_to_ad(2071, 5, 28), (2014, 9, 13))
        self.assertEqual(_bs_to_ad(2071, 6, 28), (2014, 10, 14))
        self.assertEqual(_bs_to_ad(2071, 7, 28), (2014, 11, 14))
        self.assertEqual(_bs_to_ad(2071, 8, 28), (2014, 12, 14))
        self.assertEqual(_bs_to_ad(2071, 9, 28), (2015, 1, 12))
        self.assertEqual(_bs_to_ad(2071, 10, 28), (2015, 2, 11))
        self.assertEqual(_bs_to_ad(2071, 11, 28), (2015, 3, 12))
        self.assertEqual(_bs_to_ad(2071, 12, 28), (2015, 4, 11))

    def test_conversion_to_bs(self):
        self.assertEqual(_ad_to_bs(2015, 1, 23), (2071, 10, 9))
        self.assertEqual(_ad_to_bs(2015, 2, 23), (2071, 11, 11))
        self.assertEqual(_ad_to_bs(2015, 3, 23), (2071, 12, 9))
        self.assertEqual(_ad_to_bs(2015, 4, 23), (2072, 1, 10))
        self.assertEqual(_ad_to_bs(2015, 5, 23), (2072, 2, 9))
        self.assertEqual(_ad_to_bs(2015, 6, 23), (2072, 3, 8))
        self.assertEqual(_ad_to_bs(2015, 7, 23), (2072, 4, 7))
        self.assertEqual(_ad_to_bs(2015, 8, 23), (2072, 5, 6))
        self.assertEqual(_ad_to_bs(2015, 9, 23), (2072, 6, 6))
        self.assertEqual(_ad_to_bs(2015, 10, 23), (2072, 7, 6))
        self.assertEqual(_ad_to_bs(2015, 11, 23), (2072, 8, 7))
        self.assertEqual(_ad_to_bs(2015, 12, 23), (2072, 9, 8))

        self.assertEqual(_ad_to_bs(2016, 1, 28), (2072, 10, 14))
        self.assertEqual(_ad_to_bs(2016, 2, 28), (2072, 11, 16))
        self.assertEqual(_ad_to_bs(2016, 3, 28), (2072, 12, 15))
        self.assertEqual(_ad_to_bs(2016, 4, 28), (2073, 1, 16))
        self.assertEqual(_ad_to_bs(2016, 5, 28), (2073, 2, 15))
        self.assertEqual(_ad_to_bs(2016, 6, 28), (2073, 3, 14))
        self.assertEqual(_ad_to_bs(2016, 7, 28), (2073, 4, 13))
        self.assertEqual(_ad_to_bs(2016, 8, 28), (2073, 5, 12))
        self.assertEqual(_ad_to_bs(2016, 9, 28), (2073, 6, 12))
        self.assertEqual(_ad_to_bs(2016, 10, 28), (2073, 7, 12))
        self.assertEqual(_ad_to_bs(2016, 11, 28), (2073, 8, 13))
        self.assertEqual(_ad_to_bs(2016, 12, 28), (2073, 9, 13))

        self.assertEqual(_ad_to_bs(2021, 1, 15), (2077, 10, 02))
        self.assertEqual(_ad_to_bs(2021, 2, 15), (2077, 11, 03))
        self.assertEqual(_ad_to_bs(2021, 3, 15), (2077, 12, 02))
        self.assertEqual(_ad_to_bs(2021, 4, 15), (2078, 1, 02))
        self.assertEqual(_ad_to_bs(2021, 5, 15), (2078, 2, 01))
        self.assertEqual(_ad_to_bs(2021, 6, 15), (2078, 3, 01))
        self.assertEqual(_ad_to_bs(2021, 7, 15), (2078, 3, 31))
        self.assertEqual(_ad_to_bs(2021, 8, 15), (2078, 4, 31))
        self.assertEqual(_ad_to_bs(2021, 9, 15), (2078, 5, 30))
        self.assertEqual(_ad_to_bs(2021, 10, 15), (2078, 6, 29))
        self.assertEqual(_ad_to_bs(2021, 11, 15), (2078, 7, 29))
        self.assertEqual(_ad_to_bs(2021, 12, 15), (2078, 8, 29))

    def test_invalid_date(self):
        with self.assertRaises(ValueError):
            _ad_to_bs(1983, 2, 30)