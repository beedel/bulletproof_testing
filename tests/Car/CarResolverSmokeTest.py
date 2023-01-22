import unittest
from unittest.mock import MagicMock

from src.Car.CarRepository import CarRepository
from src.Car.CarResolver import CarResolver, CarNotFoundException


class CarResolverSmokeTest(unittest.TestCase):
    def setUp(self):
        # Create a mock for the car API client
        self.car_api_client = MagicMock()
        # Initialise the car repository
        self.car_repository = CarRepository(True)
        # Crate the car resolver with the mocked API client
        self.car_resolver = CarResolver(self.car_repository, self.car_api_client)

    def test_get_all_cars_success(self):
        # Arrange
        self.car_api_client.manifacturer_is_not_bankrupt.return_value = True

        # Act
        cars = self.car_resolver.get_all_cars('Ford')

        # Assert
        self.assertEqual(['Mustang', 'Fiesta', 'Focus'], cars)

    def test_get_all_cars_failure(self):
        self.car_api_client.manifacturer_is_not_bankrupt.return_value = False
        self.assertRaises(CarNotFoundException, self.car_resolver.get_all_cars, 'manufacturer')


if __name__ == '__main__':
    unittest.main()
