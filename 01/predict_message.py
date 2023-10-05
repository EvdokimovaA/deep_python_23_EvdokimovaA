from random import uniform


class SomeModel:
    def predict(self, message: str) -> float:
        message = message + "))"
        return uniform(0, 1)


def predict_message_mood(
        message: str,
        model: SomeModel,
        bad_thresholds: float = 0.3,
        good_thresholds: float = 0.8,
) -> str:
    if bad_thresholds > good_thresholds:
        raise ValueError
    predict = model.predict(message)
    if predict > good_thresholds:
        return "отл"
    if predict < bad_thresholds:
        return "неуд"
    return "норм"
