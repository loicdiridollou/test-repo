from test_repo.module.file import function_three


def test_function_three() -> None:
    assert function_three() == "New function three"
