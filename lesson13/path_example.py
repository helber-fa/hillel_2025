import os
import pathlib

current_dir = pathlib.Path().absolute()
lesson_folder_full_path = current_dir.parent
print(lesson_folder_full_path)

#правильно з'єднує шлях відповідно до операційної системи
full_pass_to_lesson_7 = os.path.join(lesson_folder_full_path, "lesson7")
print("Lesson 7 full pass", full_pass_to_lesson_7)

print(type(current_dir))
print(current_dir)
print(current_dir.name)
print(current_dir.parent)

parents = current_dir.parents

for par in parents:
    print(par.name)
print("For directory lesson7:")
for path_ in pathlib.Path(full_pass_to_lesson_7).iterdir():
    if path_.is_file():
        print(path_.name)

print("-"*80)

for path_ in pathlib.Path(full_pass_to_lesson_7).iterdir():
    if path_.is_dir():
        print(path_.name)

print("For current directory:")
print("-"*80)


for path_ in current_dir.iterdir():
    if path_.is_file():
        print(path_.name)

print("-"*80)

for path_ in current_dir.iterdir():
    if path_.is_dir():
        print(path_.name)

test_folder_path = pathlib.Path(os.path.join(str(current_dir), "test_folder"))
print(test_folder_path)
print(test_folder_path.exists())

test_folder_path.mkdir(exist_ok=True)
print(test_folder_path.exists())

# new_folder_with_three = pathlib.Path("C:\\Users\\Helber\\PycharmProjects\\hillel_2025\\lesson13\\level1\\another_sub_folder\\target_folder")
# print("is exist: ",new_folder_with_three.exists())
# new_folder_with_three.mkdir(parents=True, exist_ok=True)
# print("is exist: ",new_folder_with_three.exists())
#
# print("-"*80)
#
# new_folder_with_three.rmdir()
# print("is exist: ",new_folder_with_three.exists())