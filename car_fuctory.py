import datetime

from engine_factory import ExtendedEngine


class Car():
    """Class that realize abstract car object"""

    amount_of_cars = 0

    def __init__(self, *args, **kwargs):
        """Initial method

        Keyword arguments:
        type -- Type of a car (default Wagon)
        model -- Model of car (default R Plus)
        color -- Color of car (default White)
        engine -- Engine for this car (default ExtendedEngine())
        """

        self._type = kwargs.get("type", "Wagon")
        self._model = kwargs.get("model", "R Plus")
        self._color = kwargs.get("color", "White")
        self._engine = kwargs.get("engine", ExtendedEngine())

        self._win_code = self._create_win_code()

        Car.amount_of_cars += 1

    def _create_win_code(self) -> str:
        """Creates win code for car instance"""

        today = datetime.datetime.today()

        win_code = '{A}-{B}-{CCCC}-{DD}-{EEEEEEE}'.format(
            A=self._type[0],
            B=self._color[0],
            CCCC=today.strftime('%Y'),
            DD=today.strftime('%m'),
            EEEEEEE=today.strftime('%w%f')
        )

        return win_code

    @classmethod
    def show_amount_of_cars(cls):
        print(f'There are {cls.amount_of_cars} cars!')

    def show_win_code(self):
        print(self._win_code)

    def __del__(self):
        Car.amount_of_cars -= 1


if __name__ == '__main__':
    car1 = Car()
    car1.show_win_code()
    car2 = Car()
    car2.show_win_code()
    car3 = Car()
    car3.show_win_code()

    Car.show_amount_of_cars()

    del car2

    Car.show_amount_of_cars()
