import sys
from src.Car.CarResolver import CarResolver
from src.Car.CarApiClient import CarApiClient
from src.Car.CarRepository import CarRepository

"""
To run the application, type:

    python3 main.py ManufacturerName
    
on the command line and hit enter.

Available manufacturers: Ford, BMW, Honda, Tesla.
"""


def main(car_resolver):
    if len(sys.argv) < 2:
        exit('Add an argument')
    print(car_resolver.get_all_cars(sys.argv[1]))


"""
Initialize everything...
P.S. Never commit your API keys to your codebase! These should be added using environment variables on the server.
"""
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
