import logging

logging.basicConfig(level=logging.ERROR)


class InvalidNameError(Exception):
    pass


class InvalidAgeError(Exception):
    pass


class InvalidIdError(Exception):
    pass


class Person:
    def __init__(self, last_name, first_name, patronymic, age):
        if not isinstance(last_name, str) or not last_name:
            logging.error("Invalid last name provided.")
            raise InvalidNameError("Invalid last name provided.")
        if not isinstance(first_name, str) or not first_name:
            logging.error("Invalid first name provided.")
            raise InvalidNameError("Invalid first name provided.")
        if not isinstance(patronymic, str) or not patronymic:
            logging.error("Invalid patronymic provided.")
            raise InvalidNameError("Invalid patronymic provided.")
        if not isinstance(age, int) or age <= 0:
            logging.error("Invalid age provided.")
            raise InvalidAgeError("Invalid age provided.")

        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.age = age

    def birthday(self):
        self.age += 1


class Employee(Person):
    def __init__(self, last_name, first_name, patronymic, age, employee_id):
        super().__init__(last_name, first_name, patronymic, age)

        if not isinstance(employee_id, int) or not (100000 <= employee_id <= 999999):
            logging.error("Invalid employee ID provided.")
            raise InvalidIdError("Invalid employee ID provided.")

        self.employee_id = employee_id

    def get_level(self):
        id_sum = sum(int(digit) for digit in str(self.employee_id))
        return id_sum % 7
