import unittest
from unittest.mock import MagicMock

from src.Car.CarResolver import CarResolver, CarNotFoundException


class CarResolverTest(unittest.TestCase):
    def setUp(self):
        #todo: mock car_api_client and car_repository
        self.car_api_client = MagicMock()
        self.car_repository = MagicMock()
        self.car_resolver = CarResolver(self.car_repository, self.car_api_client)

    def test_get_all_cars_success(self):
        # todo: set up mock values
        # Arrange
        self.car_api_client.manifacturer_is_not_bankrupt.return_value = True
        self.car_repository.find_all_cars.return_value = 'some cars'

        #todo: execute method
        # Act
        cars = self.car_resolver.get_all_cars('manufacturer')

        # Assert
        self.assertEqual(cars, 'some cars')

    def test_get_all_cars_failure(self):
        self.car_api_client.manifacturer_is_not_bankrupt.return_value = False
        self.assertRaises(CarNotFoundException, self.car_resolver.get_all_cars, 'manufacturer')

