import unittest
from unittest.mock import MagicMock

from src.CarResolver import CarResolver, BankruptManufacturerException


class CarResolverTest(unittest.TestCase):
    def setUp(self):
        # Create a mock for the car API client
        self.car_api_client = MagicMock()
        # Create a mock for the car repository
        self.car_repository = MagicMock()
        # Crate the car resolver with mocked repository and API client
        self.car_resolver = CarResolver(self.car_repository, self.car_api_client)

    def test_get_all_cars_success(self):
        # Arrange
        self.car_api_client.manifacturer_is_not_bankrupt.return_value = True
        self.car_repository.find_all_cars.return_value = 'some cars'

        # Act
        cars = self.car_resolver.get_all_cars('manufacturer')

        # Assert
        self.assertEqual(cars, 'some cars')

    def test_get_all_cars_failure(self):
        self.car_api_client.manifacturer_is_not_bankrupt.return_value = False
        self.assertRaises(BankruptManufacturerException, self.car_resolver.get_all_cars, 'manufacturer')

