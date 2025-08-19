class User:  # всі класи успадковуються від object
    def __init__(self, name, password, site_url):
        self.name = name
        self.password = password
        self.site_url = site_url
        self.finished_courses = []
        self.height = 175


    def __str__(self):
        return f"User: {self.name}, url: {self.site_url}"

    def __repr__(self):
        return f"User(name={self.name}, password={self.password}, site_url={self.site_url})"

    def __len__(self):
        return len(self.finished_courses)

    def __eq__(self, other):
        return self.height == other.height and self.finished_courses == other.finished_courses

    def __gt__(self, other):
        if isinstance(other, User):
            return self.height > other.height
        return False

    def __ge__(self, other):
        if isinstance(other, User):
            return self.height >= other.height
        return False





alex = User("Alex", "alex", "google.com")
den = User("Den", "alex", "google.com")
alex.height = 185
den.height = 195

print(alex>=5)
print(alex<den)

# string_user = str(st)
# print(len(st))
# alex.finished_courses.append("phil")
# alex.finished_courses.append("math")
# den.finished_courses.append("math")
# den.finished_courses.append("phil")
# st.finished_courses.append("phil")
# print(len(st))



