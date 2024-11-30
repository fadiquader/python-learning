import pytest
from car import Car

@pytest.fixture
def car_instance():
    return Car("BYD", "spa", 2025)

def test_car_year(car_instance):
    assert car_instance.year == 2025

def test_car_make(car_instance):
    assert car_instance.make == "BYD"
