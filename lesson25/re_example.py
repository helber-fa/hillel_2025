import re
lorem_ipsum_string = (f"Lorem ipsum dolor sit amet, consectetur adipiscing\n"
                      f" elit, sed do eiusmod tempor incididunt ut")

lorem_ipsum_string.startswith("Lorem")
lorem_ipsum_string.endswith("ut")
lorem_ipsum_string.find("sed do")
print("eiusmod" in lorem_ipsum_string)

text = ["225.3B USD", "225.3B and 550 USD", "225 322 555 000 usd"]

row1 = "Company has 225.3B USD yearly income"
row2 = "Company has 225.3B and 550 USD yearly income"
row3 = "Company has 225 322 555 000 yearly income usd"

pattern = r"225.?3\s?[B]?([\s\w\s\d\d])+\s\b(USD|usd)\b"

is_number_in_text = re.search(pattern, row1)
assert is_number_in_text, "Can not find 225.3B"
print(is_number_in_text.group())
pass