import requests


class Person:
    name = None
    cpf = None


class CpfProvider:
    server = None
    port = None


class Car:
    def __init__(self, brand):
        self.__brand = brand
        self.__rented = False

    def rent(self):
        if self.__rented is False:
            self.__rented = True

    def is_rented(self):
        return self.__rented


class CarRenting:
    def set_cpf_provoder(self, provider: CpfProvider):
        self.__url = f"http://{provider.server}:{provider.port}"

    def __person_verification(self, person: Person):
        endpoint = f"{self.__url}/validate"
        data = {"name": person.name, "cpf": person.cpf}
        content = requests.request(method="POST", url=endpoint, data=data).json()
        return content.get("status").lower() == "ok"

    def rent_car(self, person: Person, car: Car):
        result = False
        if self.__person_verification(person):
            car.rent()
            result = True
        return result


def test_validate_person():
    person = Person()
    person.name = "Joana"
    person.cpf = "123"

    car_renting = CarRenting()
    cpf_provider = CpfProvider()
    cpf_provider.server = "127.0.0.1"
    cpf_provider.port = 5001
    car_renting.set_cpf_provoder(cpf_provider)

    car = Car("Fox")
    assert car_renting.rent_car(person, car) is True
    assert car.is_rented() is True
