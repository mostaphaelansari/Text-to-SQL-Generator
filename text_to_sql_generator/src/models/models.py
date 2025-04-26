# text_to_sql_generator/src/models/models.py

class DummyTextToSQLModel:
    def __init__(self):
        print("Dummy model initialized.")

    def predict(self, text_query: str) -> str:
        """Generate a fake SQL query from a text query."""
        text_query = text_query.lower()

        # Very basic rules
        if "employees" in text_query:
            return "SELECT * FROM employees;"
        elif "customers" in text_query:
            return "SELECT * FROM customers;"
        elif "products" in text_query:
            return "SELECT * FROM products;"
        else:
            return "SELECT * FROM unknown_table;"
