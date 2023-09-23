import pytest
from predict_message import SomeModel, predict_message_mood


@pytest.mark.parametrize(
    "message, model, result",
    [
        ("message", SomeModel(0.1), "неуд"),
        ("message", SomeModel(0.0), "неуд"),
        ("message", SomeModel(0.3), "норм"),
        ("message", SomeModel(0.4), "норм"),
        ("message", SomeModel(0.8), "норм"),
        ("message", SomeModel(0.9), "отл"),
        ("message", SomeModel(1.0), "отл")
    ]
)
def test_predict_message_mood(message, model, result):
    assert predict_message_mood(message, model) == result
