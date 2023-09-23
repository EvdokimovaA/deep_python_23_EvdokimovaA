class SomeModel:
    def __init__(self, number: float):
        self.number = number

    def predict(self, message: str) -> float:
        message = message + ")))"
        return self.number


def predict_message_mood(
        message: str,
        model: SomeModel,
        bad_thresholds: float = 0.3,
        good_thresholds: float = 0.8,
) -> str:
    predict = model.predict(message)
    if predict > good_thresholds:
        return "отл"
    if predict < bad_thresholds:
        return "неуд"
    return "норм"
