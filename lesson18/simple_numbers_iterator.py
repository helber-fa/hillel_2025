class SimpleNumberIterator:
    def __init__(self, quantity_simple_numbers):
        self.__cur_num = 2
        self.quantity_simple_numbers = quantity_simple_numbers
        self.__quantity_returned = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.quantity_simple_numbers == self.__quantity_returned:
            raise StopIteration
        self.__get_simple_number()
        self.__quantity_returned = self.__quantity_returned + 1
        return self.__cur_num

    def __get_simple_number(self):
        while True:
            self.__cur_num += 1
            if self.__is_prime(self.__cur_num):
                return self.__cur_num

    def __is_prime(self, number):
        for k in range(2, number-1):
            if number % k == 0:
                return False
        return True

for num in SimpleNumberIterator(15):
    print(num)


