import os



def is_dev():
    return os.getenv("CURRENT_ENV", "PROD") == "DEV"

def validate_test_case(test_case):
    error = []

    if not test_case.get("id"):
        error.append("ID is missing")
    elif not test_case["id"].startswith("TC"):
        error.append("Wrong Id name")

    if not test_case.get("title"):
        error.append("Title is empty")

    return error