if True:
    print("Hello")

# and(&), or(|), is(==), not(!=), >, <
# a = 5
# b = 6
# c = 7
# if a > b or c > b:
#     print("A is bigger than B or C > B")
#
# if a < b and c > b:
#     print("We can see this")
# else:
#     print("Something goes wrong")

# поверне False
print(bool([]))
print(bool(dict()))
print(bool(0))
print(bool(""))

response = []
if not response:
    print("Empty response")

card_number = 2222244444477777
cvv = 788

if card_number == 2222244444477777 and cvv == 789:
    print("Trx complete")
else:
    if card_number !=2222244444477777:
        print("Wrong card number")
    elif cvv != 789:
        print("Wrong cvv")
    print("Trx failed")





