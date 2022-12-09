import pathlib

practice_file = pathlib.Path.cwd()
print(practice_file)
new_folder = practice_file / "practice_file_folder"
new_folder2 = new_folder / "documents"
new_folder3 = new_folder / "images"

new_folder.mkdir()
new_folder2.mkdir()
new_folder3.mkdir()

print(new_folder.exists())
print(new_folder3.exists())

files = [new_folder3 / "image_1.png",
         new_folder3 / "image_2.gif",
         new_folder3 / "image_3.png",
         new_folder3 / "image_4.jpg"]

for count in files:
    count.touch()
print(files)
