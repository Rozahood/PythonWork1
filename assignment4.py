import pathlib

my_folder = pathlib.Path.home()
print(my_folder)
new_folder = "C:" / "Users" / "ADMIN" / "PycharmProjects" / "cohort14.py" / "my_works" / "my_folder"
new_folder2 = "C:" / "Users" / "ADMIN" / "PycharmProjects" / "cohort14.py" / "my_works" / "my_folder/ images"

new_folder.mkdir()
new_folder2.mkdir()

print(new_folder.exists())
print(new_folder2.exists())

files = ["C:" / "Users" / "ADMIN" / "PycharmProjects" / "cohort14.py" / "my_works" / "my_folder" / "file1.txt",
         "C:" / "Users" / "ADMIN" / "PycharmProjects" / "cohort14.py" / "my_works" / "my_folder" / "file2.txt"]

for count in files:
    count.touch()
print(files)

files = ["C:" / "Users" / "ADMIN" / "PycharmProjects" / "cohort14.py" / "my_works" / "my_folder/ images" / "image1.png"]
for count in files:
    count.touch()
print(files)
