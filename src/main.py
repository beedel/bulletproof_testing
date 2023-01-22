import sys
from src.Car.CarResolver import CarResolver
from src.Car.CarApiClient import CarApiClient
from src.Car.CarRepository import CarRepository


def main(car_resolver):
    if len(sys.argv) < 2:
        exit('Add an argument')
    print(car_resolver.get_all_cars(sys.argv[1]))


if __name__ == "__main__":
    main(
        car_resolver=CarResolver(
            car_api_client=CarApiClient(
                api_key='adsf2354adf4Xadf',
            ),
            car_repository=CarRepository(
                db_connection=True,
            ),
        ),
    )
