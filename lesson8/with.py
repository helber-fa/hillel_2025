with open("main") as f: # contex manager
    print(f.read())

# f1 = open("main")
# f2 = open("main")

try:
    f = open("main")
    print(f.read())
finally:
    f.close()
# print(f1.read())
# f1.close()
