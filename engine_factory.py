import datetime


class Engine:
    """This is a class representing the abstraction of the engine."""

    def __init__(self, *args, **kwargs):
        """Initialize the engine object.

        Keyword arguments:
        model_name -- Model name of engine (default M111 E23 / E23 ML)
        number_of_cylinders -- Amount of cilindera (default 4)
        engine_displacement -- Engine displacement (default 2)
        engine_resource -- Engine resource in kilometers (default 200000)
        fuel_type -- Petrol or diesel (default petrol)
        """

        self._model_name = kwargs.get('model_name', 'M111 E23 / E23 ML')
        self._number_of_cylinders = kwargs.get('number_of_cylinders', 4)
        self._engine_displacement = kwargs.get('engine_displacement', 2)
        self._engine_resource = kwargs.get('engine_resource', 200_000)
        self._fuel_type = kwargs.get('fuel_type',  'petrol')

    def info(self):
        """This method represents engine information."""

        print(
            f"Model name is {self._model_name}",
            f"Number os cilinders is {self._number_of_cylinders}",
            f"Engine displacement is {self._engine_displacement}",
            f"Engine resource is {self._engine_resource}",
            f"Fuel type is {self._fuel_type}",
            sep='\n'
        )


class ExtendedEngine(Engine):
    """This class is extansion of Engine class."""

    def __init__(self, *args, **kwargs):
        """Initialize the extended engine object.

        Keyword arguments:
        model_name -- Model name of engine (default M111 E23 / E23 ML)
        number_of_cylinders -- Amount of cilindera (default 4)
        engine_displacement -- Engine displacement (default 2)
        engine_resource -- Engine resource in kilometers (default 200000)
        fuel_type -- Petrol or diesel (default petrol)
        current_engine_mileage -- Mileage in kilometers (default 0)
        """

        super().__init__(*args, **kwargs)

        self._current_engine_mileage = kwargs.get('current_engine_mileage', 0)
        self._unique_number = self.create_unique_number()

    @staticmethod
    def create_unique_number() -> int:
        """Static method that creates unique number for engine object"""

        today = datetime.datetime.today()
        unique_number_str = today.strftime('%Y%m%d%H%M%S%f')

        return int(unique_number_str)

    def get_unique_number(self):
        return self._unique_number

    def increase_mileage(self, kilometers: int):
        """Increases current_engine_mileage

        Arguments:
        kilometers -- amount of kilometers by witch
                      the mileage will be increase
        """

        if kilometers > 0:
            self._current_engine_mileage += kilometers

    def get_remain_engine_resource(self) -> int:
        "Returns remain engine resource"

        result = self._engine_resource - self._current_engine_mileage
        return 0 if result < 1 else result

    def info(self):
        """This method represents engine information."""

        super().info()
        print(
            f"Unique number is {self._unique_number}",
            f"Remain engine resource is {self.get_remain_engine_resource()}",
            sep='\n'
        )


if __name__ == '__main__':

    engine = Engine()
    engine.info()

    print('-' * 35)

    ext_engine = ExtendedEngine(
        engine_resource=350_000
    )
    ext_engine.increase_mileage(12345)

    ext_engine.info()

    print('-' * 35)

    ext_engine2 = ExtendedEngine()
    ext_engine2.info()
