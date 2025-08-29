import pytest

class TestSomething:
    def test_something(self, pre_and_post_conditions):
        print("test1 is running...")

    def test_something_without_gen(self):
        print("test2 is running...")

    @pytest.fixture()
    def pre_and_post_conditions(self):
        print("Pre conditions")
        yield
        print("Post Conditions")