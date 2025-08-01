import csv

# Дані для запису у CSV-файл
data = [
    ['Name', 'Age', 'City', "Boolean"],
    ['John', 30, 'New York', True],
    ['Alice', 25, 'Los Angeles', False],
    ['Bob', 35, 'Chicago', None]
]

# Відкриття CSV-файлу для запису
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

with open('output.csv', newline='') as csvfile:
    # reader = csv.reader(csvfile)
    reader = list(csv.reader(csvfile))

    header = reader[0]
    row_data = reader[1:]
    print("Header is:", header)
    for i, row in enumerate(row_data, start=1):
        print(f"Row number - {i} with data: {row}")