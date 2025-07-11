def greeting(first_name: str, second_name: str) -> str :
    """
    This function format our greeting
    :param first_name: Name of person
    :param second_name: Surname of person
    :return: string, Formated line
    """
    formatted_string = f"Hello {first_name.upper()}, {second_name.upper()}"
    print(formatted_string)
    return formatted_string
    # якщо не вказаний return то дефолтно return None



for full_name in [("Alex", "Rudyk"), ("John", "Doy")]:
    greeting(full_name[0], full_name[1])

for full_name in [("Alex", "Rudyk"), ("John", "Doy")]:
    greeting(second_name=full_name[0], first_name=full_name[1])
