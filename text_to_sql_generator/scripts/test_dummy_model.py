# text_to_sql_generator/scripts/test_dummy_model.py

import sys
from pathlib import Path

# Add project root to path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from text_to_sql_generator.src.models.models import DummyTextToSQLModel

if __name__ == "__main__":
    model = DummyTextToSQLModel()

    questions = [
        "Show me all employees",
        "List all customers",
        "Give me all products",
        "What is in the database?"
    ]

    for question in questions:
        sql = model.predict(question)
        print(f"Input: {question}\nGenerated SQL: {sql}\n")
