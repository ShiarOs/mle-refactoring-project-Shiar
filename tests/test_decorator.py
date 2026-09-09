import logging

from src.decorators import log_step


def test_log_step_returns_original_result():
    @log_step
    def add_numbers(first_number, second_number):
        return first_number + second_number

    result = add_numbers(2, 3)

    assert result == 5


def test_log_step_preserves_function_name():
    @log_step
    def example_function():
        return "done"

    assert example_function.__name__ == "example_function"


def test_log_step_writes_log_messages(caplog):
    @log_step
    def example_function():
        return "done"

    with caplog.at_level(logging.INFO):
        result = example_function()

    assert result == "done"
    assert "Starting example_function" in caplog.text
    assert "Finished example_function" in caplog.text