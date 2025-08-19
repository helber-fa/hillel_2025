class Filters:
    #  ?age_gte=20&score=40
    def __init__(self, **kwargs):
        for k,v in kwargs.items():
            setattr(self, k, v)

    def __eq__(self, other):
        for k in [k for k in self.__dict__ if k is not None]:
            if self.__dict__[k] != getattr(other, k, None):
                return False
        return True

filter1 = Filters(**{"age_gte": 20, "score": 40})
filter2 = Filters(**{"age_gte": 20, "score": 40, "some_filter": 1})

print(filter2 == filter1)