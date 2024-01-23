import random
from functools import cache


@cache
def build_grammar_data():
    grammar_data = []

    with open("data/grammar.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        if not line.startswith(" "):
            line_cleaned = line.strip()
            line_cleaned = line_cleaned[line_cleaned.find(".") + 2 :]
            grammar_data.append(
                {"title": line_cleaned, "examples": [], "completed_at": None}
            )
        else:
            line_cleaned = line.strip()
            line_cleaned = line_cleaned[line_cleaned.find(".") + 2 :]
            grammar_data[-1]["examples"].append(line_cleaned)

    random.shuffle(grammar_data)

    return grammar_data


@cache
def build_study_data():
    grammar_data = build_grammar_data()
    if len(grammar_data) % 3 != 0:
        assert False, "The number of grammar points is not divisible by 3"

    study_data = []

    for i in range(0, len(grammar_data), 3):
        study_data.append(
            {
                "grammar_1": grammar_data[i]["title"],
                "grammar_1_index": i,
                "grammar_1_examples": grammar_data[i]["examples"],
                "grammar_2": grammar_data[i + 1]["title"],
                "grammar_2_examples": grammar_data[i + 1]["examples"],
                "grammar_2_index": i + 1,
                "grammar_3": grammar_data[i + 2]["title"],
                "grammar_3_examples": grammar_data[i + 2]["examples"],
                "grammar_3_index": i + 2,
                "completed": False,
            }
        )
    return study_data


def build_review(current_study_data):
    grammar_data = build_grammar_data()
    study_data = build_study_data()

    completed_study_data = [study for study in study_data if study["completed"]]
    completed_grammar_indexes = [
        current_study_data["grammar_1_index"],
        current_study_data["grammar_2_index"],
        current_study_data["grammar_3_index"],
    ]
    for study in completed_study_data:
        completed_grammar_indexes.append(study["grammar_1_index"])
        completed_grammar_indexes.append(study["grammar_2_index"])
        completed_grammar_indexes.append(study["grammar_3_index"])

    review = []
    for j in range(0, 10):
        random_grammar_index = random.choice(completed_grammar_indexes)
        random_example = random.choice(grammar_data[random_grammar_index]["examples"])

        if random_example not in review:
            review.append(random_example)

    return review
