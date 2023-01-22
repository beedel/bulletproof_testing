# exclude from mutation testing
from src.Car.Exception.DatabaseConnectionException import DatabaseConnectionException

"""
This class mimics the behaviour of a repository class that has a database connection.
In the real world, the repository class would have some SQL that would return whatever values you ask for.
For the purposes of this workshop, it simply has an attribute 'cars', that holds the values 
the actual database call would return.
"""


class CarRepository:

    def __init__(self, db_connection) -> None:
        self.db_connection = db_connection
        self.cars = {
            'Ford': ['Mustang', 'Fiesta', 'Focus'],
            'BMW': ['M3', 'X5', 'iX'],
            'Honda': ['Civic', 'Jazz', 'E'],
        }

    def find_all_cars(self, manufacturer):
        # TODO: random int
        if self.db_connection:
            return self.cars[manufacturer]
        else:
            raise DatabaseConnectionException('Database connection lost!')
