class User:
    def __init__(self, name, password, site_url):
        self.name = name
        self.password = password
        self.site_url = site_url

    def login(self):
        print(f"User {self.name} was logged in {self.site_url}")

    def logout(self):
        print(f"User {self.name} was logged out {self.site_url}")

dev_user = User("dev_user", "dev-password", "http://dev-something.org")
stage_user = User("stage_user", "stage_user", "http://stage-something.org")
prod_user = User("prod_user", "prod_user", "http://prod-something.org")


print(dev_user.name) # атрибут
dev_user.login() #метод
dev_user.logout()
