import pandas as pd
from interview_gen.question_bank import load_seed_question_bank

REQUIRED_COLUMNS = {"question", "category", "topic", "difficulty"}


def test_load_seed_question_bank_returns_dataframe_with_required_columns():
    bank = load_seed_question_bank()
    assert isinstance(bank, pd.DataFrame)
    assert REQUIRED_COLUMNS <= set(bank.columns)


def test_load_seed_question_bank_has_at_least_15_questions():
    bank = load_seed_question_bank()
    assert len(bank) >= 15


def test_load_seed_question_bank_has_both_categories():
    bank = load_seed_question_bank()
    assert set(bank["category"].unique()) == {"technical", "behavioral"}


def test_load_seed_question_bank_questions_are_unique():
    bank = load_seed_question_bank()
    assert bank["question"].nunique() == len(bank)
