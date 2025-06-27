string_var = "Alex"

age = 20
lorem_ipsum_string = (f"Lorem ipsum dolor sit amet,{age + 70} consectetur adipiscing\n"
                      f" {string_var} elit, sed do eiusmod tempor incididunt ut")

# відображає стрінгу в тому вигляді в якому це записано
r_string = (r"Lorem ipsum dolor sit\  '  amet,{age + 70} consectetur adipiscing\n"
            r" {string_var} elit, sed do eiusmod tempor incididunt ut")

age = 25
print(r_string)

# input завжди повертає string
# age = input("Enter your age: ")

print(f"Your age is: {age}")