def __setattr__(self, key, value):
    if key == "score":
        if not (100 >= value >= 0):
            print("Score must be between 0 and 100. Set 0")
            value = 0
    super().__setattr__(key, value)