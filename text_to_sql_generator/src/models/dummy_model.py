class DummyTextToSQLModel:
    def __init__(self):
        pass

    def predict(self, user_question: str) -> str:
        # For now, no real intelligence
        return "SELECT * FROM employees;"
