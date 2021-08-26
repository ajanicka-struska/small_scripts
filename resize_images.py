import os
from PIL import Image


def give_path():
    return (input("Path to folder:\n")).replace("\"", "")


def create_newfolder(path):
    try:
        os.mkdir(path + "\\m")
        print("Folder created!")
    except FileExistsError:
        print("Folder already exists!")


def check_files(f):
    files = [i for i in os.listdir(f) if os.path.isfile(os.path.join(f, i))]
    return [j for j in files if j[-4:] == ".png"]


if __name__ == "__main__":
    path_to_folder = give_path()
    create_newfolder(path_to_folder)
    path_to_newfolder = path_to_folder + "\\m\\"
    l_files = check_files(path_to_folder)
    size = 800

    for i in l_files:
        j = i.split(".")[0]
        image = Image.open(path_to_folder + "\\" + i)
        what_percent = size/float(image.size[0])
        height = int(float(image.size[1]) * float(what_percent))
        img = image.resize((size, height), Image.ANTIALIAS)
        img.save(path_to_newfolder + j + "m.png", "PNG")
        print(f"Image {i} resized!")



