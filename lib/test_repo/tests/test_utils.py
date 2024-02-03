"""Test module."""

from test_repo.utils import function_one


def test_function_one() -> None:
    """Test."""
    assert function_one() == "test"
