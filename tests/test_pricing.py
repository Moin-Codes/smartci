import pytest

from src.pricing import add_tax, apply_discount


def test_apply_discount_calculates_discount():
	assert apply_discount(100, 20) == 90


def test_apply_discount_at_zero_percent():
	assert apply_discount(100, 0) == 100


def test_apply_discount_at_one_hundred_percent():
	assert apply_discount(100, 100) == 0


@pytest.mark.parametrize("discount", [-1, 101])
def test_apply_discount_rejects_invalid_discount(discount):
	with pytest.raises(ValueError):
		apply_discount(100, discount)


def test_add_tax_uses_default_tax_rate():
	assert add_tax(100) == pytest.approx(118)
