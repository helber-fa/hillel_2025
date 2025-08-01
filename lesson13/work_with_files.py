file_path = "file_for_read_write.txt"
file_path_append = "file_for_append.txt"

# r - читання
# w - режим запису/перестворення файлу(перезапис)
# a - append, додавання в файл/створення файл

# r+ - read + write, файл повинен існувати
# w+ - read + write, файл може бути створений
# a+ - read + append, файл може бути створений

# with open(file_path, mode="r") as f:
#     data = f.read()
#
# with open(file_path) as f:
#     data = f.read()

# with open(file_path, mode="w") as f:
#     f.write("line1")
#     f.write("line2\n")
#     f.write("line3\n")
#     f.write(r"line3\n") #raw string
#     f.write("line3\\n") #екранування
#
# with open(file_path_append, mode="a") as f:
#     #     f.write("line1")
#     #     f.write("line2\n")
#     #     f.write("""zero line
#     #     \n first line
#     # second line
#     #
#     #
#     #
#     #             last line
#     #     """)
#     f.write("line1\n")
#     f.write(str(5))
#     f.write("\n")
#     f.writelines(["hello ", "world ", "My name is Alex\n"])
#     f.writelines([str(k) for k in range(25)])

with open(file_path_append, mode="r") as f:
    data = f.read() #поверне рядок
    print(data)
    data = f.read() #поверне пустий рядок
    print("   +", data)

with open(file_path_append, mode="r") as f:
    # data = f.readlines() #поверне список строк
    print(f.readlines()[-1])


#
# with open(file_path_append, mode="r") as f:
#     print(f.readline(4)) #поверне один рядок з 4 перших символів
    # print(f.readline()) #поверне один рядок
    # print(f.readline()) #поверне один рядок
    # print(f.readline()) #поверне один рядок
    # print(f.readline()) #поверне один рядок
    # print(f.readline()) #поверне один рядок
    # print(f.readline()) #поверне один рядок
    # print(f.readline()) #поверне один рядок
    # print(f.readline()) #поверне один рядок
    # print(f.readline()) #поверне один рядок
