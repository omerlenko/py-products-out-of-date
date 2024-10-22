import pytest
from datetime import date
from app.main import outdated_products
from unittest.mock import patch, MagicMock


@pytest.fixture()
def products() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": date(2024, 10, 20),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": date(2024, 10, 10),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": date(2024, 10, 30),
            "price": 160
        }
    ]


@pytest.mark.parametrize(
    "today_date, result_list",
    [
        (date(2024, 10, 25), ["salmon", "chicken"]),
        (date(2024, 10, 15), ["chicken"]),
        (date(2024, 10, 21), ["salmon", "chicken"]),
        (date(2024, 10, 20), ["chicken"]),
    ]
)
@patch("datetime.date")
def test_when_date_is_expired(
    mock_date: MagicMock,
    products: list,
    today_date: date,
    result_list: list
) -> None:
    mock_date.today.return_value = today_date
    assert outdated_products(products) == result_list
