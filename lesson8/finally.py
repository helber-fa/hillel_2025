users_scores = [
    {"name": "Alex", "scores": {"math": 10, "chem": 100, "phis": 10}},
    {"name": "Den", "scores": {"math": 10, "phis": 0}},
    {"name": "Ivan", "scores": {"math": 0, "chem": 0, "phis": 0}},
    {"name": "Ira", "scores": {"math": 10, "chem": None, "phis": 0}},
    {"name": "Olga", "scores": {}},
]

def get_score(user):
    scores = user.get("scores")
    sum = 0
    try:
        for s in scores:
            sum += scores[s]
        result = sum / len(scores)
    except ZeroDivisionError:
        print(f"No data for user {user["name"]}")
        return 0
    except TypeError:
        return 0
        print(f"Get None for {s}")
    else:
        print("There was no errors")
    finally:
        print(f"Finally: User have score {sum}")
    return result

for user in users_scores:
    print("_"*80)
    print(f"User name is {user["name"]}")
    print(f"User score is {get_score(user)}")