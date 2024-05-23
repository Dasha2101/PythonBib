import pytest
from Person import Person, Employee, InvalidNameError, InvalidAgeError, InvalidIdError

def test_person_init_valid():
    person = Person("Иванов", "Иван", "Иванович", 30)
    assert person.age == 30

def test_person_init_invalid_name():
    with pytest.raises(InvalidNameError):
        Person("", "Иван", "Иванович", 30)

def test_person_init_invalid_age():
    with pytest.raises(InvalidAgeError):
        Person("Иванов", "Иван", "Иванович", -1)


def test_employee_init_valid():
    employee = Employee("Петров", "Петр", "Петрович", 35, 123456)
    assert employee.employee_id == 123456

def test_employee_init_invalid_id():
    with pytest.raises(InvalidIdError):
        Employee("Сидоров", "Сидор", "Сидорович", 40, 12345)
