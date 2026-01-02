import unittest
from temperature import celsius_to_fahrenheit

class TestTemperatureConversion(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_positive(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_negative(self):
        self.assertEqual(celsius_to_fahrenheit(-40), -40)

    def test_decimal(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(36.6), 97.88, places=2)

if __name__ == '__main__':
    unittest.main()
