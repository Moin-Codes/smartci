import pytest
from src.inventory import Inventory


def test_add_stock():
    inventory = Inventory()
    inventory.add_stock("widget", 5)
    assert inventory.stock["widget"] == 5


def test_remove_stock():
    inventory = Inventory()
    inventory.add_stock("widget", 5)
    inventory.remove_stock("widget", 2)
    assert inventory.stock["widget"] == 3


def test_remove_more_stock_than_available_raises_value_error():
    inventory = Inventory()
    inventory.add_stock("widget", 5)

    with pytest.raises(ValueError):
        inventory.remove_stock("widget", 10)