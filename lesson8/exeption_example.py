import traceback

# try: # код в якому теоретично може бути помилка
#     print(1/0)
# except ZeroDivisionError: # вказуємо яку помилку ми відловлюємо
#     print("You can not divide by 0") # як ми хочемо її обробити
# print("Hello")

users = [
    {"name": "Alex", "math": 10, "chem": 0, "phis": 0},
    {"name": "Den", "math": 60,  "phis": 10},
    {"name": "Ivan", "math": 90, "chem": 10, "phis": 30},
    {"name": "Orest", "math": 50, "chem": 40, "phis": None}
]

def test_count_data(user_list):
    for k in user_list:
        # Погані варіанти захендлити помилки
        # if k["phis"] is None:
        #     print("None in phis")
        #     continue
        # if k.get("chem") is None:
        #     print("No chem")
        #     continue
        try:
            assert k["math"] + k["chem"] + k["phis"] > 0
            print(k["name"], k["math"], k["chem"], k["phis"] )
        except KeyError as error:
            # raise KeyError(error) # викликати помилку
            print(traceback.format_exc())
            print(f"No key for user: {k}")
        except TypeError as error:
            print(error)
            max()
            print(f"Bad type for user: {k}")
        except Exception as e:
            print(f"Some unexpected error: {e}")

test_count_data(users)

