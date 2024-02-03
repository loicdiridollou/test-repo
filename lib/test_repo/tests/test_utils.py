from test_repo.utils import function_one


def test_function_one() -> None:
    assert function_one() == "test"
