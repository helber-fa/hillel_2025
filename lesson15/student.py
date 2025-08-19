class User:
    def __init__(self, name, score):
        self.name = name
        if 100 >= score >= 0:
            self.score = score
        else:
            print("Score must be between 0 and 100. Set 0")
            self.score = 0

    def __str__(self):
        return f"User:{self.name}, score: {self.score}"

    def __setattr__(self, key, value):
        if key == "score":
             if not (100>= value >= 0):
                 print("Score must be between 0 and 100. Set 0")
                 value = 0
        super().__setattr__(key,value)


alex = User("Alex", -5)
print(alex)
alex.score = 1000000
print(alex)

print(alex + alex)