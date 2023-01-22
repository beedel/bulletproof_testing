import unittest

from src.Car.CarApiClient import CarApiClient


class CarApiClientTest(unittest.TestCase):
    def setUp(self):
        self.car_api_client = CarApiClient(self)

    def test_manufacturer_is_not_bankrupt(self):
        expected = True
        connected = self.car_api_client.manifacturer_is_not_bankrupt('Ford')

        self.assertEqual(connected, expected)

    def test_manufacturer_is_bankrupt(self):
        #Arrange
        expected = False
        #Act
        actual = self.car_api_client.manifacturer_is_not_bankrupt("Tesla")
        #Assert
        self.assertEqual(actual, expected)

    def test_unknown_manufacturer_raises_exception(self):
        with self.assertRaises(Exception):
            self.car_api_client.manifacturer_is_not_bankrupt('Unknown')


if __name__ == '__main__':
    unittest.main()