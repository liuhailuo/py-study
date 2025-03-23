# with open('a.txt') as f:
#     file1_data = f.read()
# with open('db.json') as f:
#     file2_data = f.read()

# with open('c.txt', 'w') as f:
#     f.write(file1_data)
#     f.write(file2_data)

file_names = ['a.txt', 'db.json', 'c.txt']

files_data = []
for file_name in file_names:
    with open(file_name, 'r') as f:
        file_data = f.read()
        files_data.append(file_data)

with open('d.txt', 'w') as f:
    for file_data in files_data:
        f.write(file_data)