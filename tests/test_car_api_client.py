import unittest

from src.Exception.ManufacturerNotFoundException import ManufacturerNotFoundException
from src.CarApiClient import CarApiClient


class CarApiClientTest(unittest.TestCase):
    def setUp(self):
        # Initialise the API client
        self.car_api_client = CarApiClient(self)

    def test_manufacturer_is_not_bankrupt(self):
        # Arrange
        expected = True

        # Act
        connected = self.car_api_client.manifacturer_is_not_bankrupt('Ford')

        # Assert
        self.assertEqual(expected, connected)

    def test_manufacturer_is_bankrupt(self):
        # Arrange
        expected = False

        # Act
        bankrupt = self.car_api_client.manifacturer_is_not_bankrupt("Tesla")

        # Assert
        self.assertEqual(expected, bankrupt)

    def test_unknown_manufacturer_raises_exception(self):
        with self.assertRaises(ManufacturerNotFoundException):
            self.car_api_client.manifacturer_is_not_bankrupt('Unknown')


if __name__ == '__main__':
    unittest.main()
