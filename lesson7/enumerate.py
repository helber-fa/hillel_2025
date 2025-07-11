for k in enumerate(["alex", "den"]):
    print(k)

for k in enumerate(["alex", "den"], start=10):
    print(k)

for k, name in enumerate(["alex", "den"], start=10):
    print(f"Name {name} have index: {k}")