import pathlib


# A simple Python function
def Precious():
    list = []
    print("Welcome to my project")


# Driver code to call a function()

    Precious = pathlib.Path.cwd()
    print("Welcome to my project")
    new_folder = Precious / "Welcome to my project"

    new_folder.mkdir(exist_ok=True)

    print(new_folder.exists())

    file = new_folder / "Project_main"
    file.touch(exist_ok=True)
    print(file.exists())

    royal = file.write_text("The class is on fire!")
    royal = file.read_text()
    print(royal)
    word = royal
    wow = royal.split(" ")
    print(wow)

    for i in royal:
        list.append(i)
    return list

print(Precious())




