import pytest
from expense_tracker.expenses import validate_amount, validate_date


def test_validate_amount_accepts_positive_number():
    assert validate_amount("12.5") == 12.5


@pytest.mark.parametrize("bad", [-5, 0, "abc", None])
def test_validate_amount_rejects_bad_values(bad):
    with pytest.raises(ValueError):
        validate_amount(bad)


def test_validate_date_accepts_valid_date():
    assert validate_date("2026-11-12") == "2026-11-12"


@pytest.mark.parametrize("bad", ["2026-13-45", "12/11/2026", "", None])
def test_validate_date_rejects_bad_values(bad):
    with pytest.raises(ValueError):
        validate_date(bad)

@pytest.mark.parametrize("bad", ["nan", "inf", "-inf", "1e999"])
def test_validate_amount_rejects_non_finite_values(bad):
    """Security: NaN and infinity must not be able to corrupt stored totals."""
    with pytest.raises(ValueError):
        validate_amount(bad)