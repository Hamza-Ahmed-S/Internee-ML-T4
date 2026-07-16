import pandas as pd

_SEED_QUESTIONS = [
    {"question": "What is the difference between a list and a tuple in Python?", "category": "technical", "topic": "Python", "difficulty": "beginner"},
    {"question": "How would you handle missing values in a dataset?", "category": "technical", "topic": "Data Analysis", "difficulty": "beginner"},
    {"question": "Explain the difference between INNER JOIN and LEFT JOIN in SQL.", "category": "technical", "topic": "SQL", "difficulty": "intermediate"},
    {"question": "What is overfitting, and how can it be prevented?", "category": "technical", "topic": "Machine Learning", "difficulty": "intermediate"},
    {"question": "Describe how you would design a REST API for a simple to-do app.", "category": "technical", "topic": "Product", "difficulty": "intermediate"},
    {"question": "What is the time complexity of binary search, and why?", "category": "technical", "topic": "Python", "difficulty": "intermediate"},
    {"question": "How do you approach debugging a failing test in an unfamiliar codebase?", "category": "technical", "topic": "Python", "difficulty": "beginner"},
    {"question": "What is the difference between supervised and unsupervised learning?", "category": "technical", "topic": "Machine Learning", "difficulty": "beginner"},
    {"question": "How would you optimize a slow SQL query?", "category": "technical", "topic": "SQL", "difficulty": "advanced"},
    {"question": "What version control workflow have you used, and why?", "category": "technical", "topic": "Project Management", "difficulty": "beginner"},
    {"question": "Tell me about a time you had to learn a new tool or technology quickly.", "category": "behavioral", "topic": "Learning", "difficulty": "beginner"},
    {"question": "Describe a situation where you disagreed with a teammate. How did you resolve it?", "category": "behavioral", "topic": "Communication", "difficulty": "beginner"},
    {"question": "Tell me about a project where you had to manage competing deadlines.", "category": "behavioral", "topic": "Workload", "difficulty": "intermediate"},
    {"question": "Describe a time you received critical feedback. How did you respond?", "category": "behavioral", "topic": "Communication", "difficulty": "beginner"},
    {"question": "Tell me about a time you made a mistake at work or school. What did you learn?", "category": "behavioral", "topic": "Learning", "difficulty": "beginner"},
    {"question": "How do you prioritize tasks when everything feels urgent?", "category": "behavioral", "topic": "Workload", "difficulty": "intermediate"},
    {"question": "Describe a time you had to explain a technical concept to a non-technical person.", "category": "behavioral", "topic": "Communication", "difficulty": "intermediate"},
    {"question": "Tell me about a time you took initiative without being asked.", "category": "behavioral", "topic": "Product", "difficulty": "beginner"},
]


def load_seed_question_bank() -> pd.DataFrame:
    """Return the starter question bank used as the 'existing question bank'
    data input and as the deduplication reference for newly generated questions."""
    return pd.DataFrame(_SEED_QUESTIONS)
