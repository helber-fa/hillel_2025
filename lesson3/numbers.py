standard = 3.10
float_with_pow = 2.0e-2

a = 0.1
b = 0.2

print(standard)
print(float_with_pow)
print(a + b)

# те як в пам'яті зберігається float
c = 1 / 5
d = 2 / 10

# піднесення до ступеня
my_int = 2 ** 5
my_int_2 = pow(2, 4)

# assert c == d
# assert 0.3 == a+b

print(my_int)
print(my_int_2)

# цілочисельне ділення
print(17 // 5)

# остача від ділення
print(17 % 5)

# побітовий зсув
print(10>>1)

a = 10
b = 2
c = 5 + pow(int(5.5), 2)
print(c)

# приорітети операцій в пайтоні співпадають з пріорітетами в математиці
print((a+b) * c)

#  = - присвоєння значення змінній
#  == - порівняння двох змінних
# & - логічне "і" може бути and
# | - логічне "або" може бути or

if a == 10:
    print("Hello")

if (a < b) or (a == 10):
    print("Hello1")

first = 10 ; second = 20




