import os
from PIL import Image
from fpdf import FPDF


def get_path():
    return (input("Write path to folder here:\n")).replace("\"", "") + "\\"


def create_newfolder(p):
    try:
        os.mkdir(f"{p}new")
        print("New folder done!")
        return f"{p}new"
    except FileExistsError:
        print("Path already exists!")
        return f"{p}new"


def read_files(old_path):
    list_of_files = os.listdir(old_path)
    return [l for l in list_of_files if os.path.isfile(os.path.join(old_path, l))]


def crop_dimensions():
    left = int(input("Left dimension:\n"))
    upper = int(input("Upper dimension:\n"))
    right = int(input("Right dimension:\n"))
    lower = int(input("Lower dimension:\n"))
    return left, upper, right, lower


def to_pdf(path_to):
    pdf = FPDF("P", "mm", "A4")
    list_images = read_files(path_to)
    for elem in list_images:
        pdf.add_page()
        pdf.image(path_to + elem, 0, 0, 210, 297)
    pdf.output(f"{path_to}new_book.pdf", "F")


if __name__ == "__main__":
    path = get_path()
    create_newfolder(path)
    path_to_new = f"{path}new\\"
    list_of_images = read_files(path)
    dimensions = tuple(crop_dimensions())

    for count, value in enumerate(list_of_images):
        image = Image.open(f"{path}\\{value}")
        image_cropped = image.crop(dimensions)
        if count < 10:
            image_cropped.save(f"{path_to_new}\\000{count + 1}.png", "PNG")
            print(f"Image{count + 1} done")
        elif 10 <= count <= 99:
            image_cropped.save(f"{path_to_new}\\00{count + 1}.png", "PNG")
            print(f"Image{count + 1} done")
        elif 100 <= count <= 999:
            image_cropped.save(f"{path_to_new}\\0{count + 1}.png", "PNG")
            print(f"Image{count + 1} done")
        else:
            image_cropped.save(f"{path_to_new}\\{count + 1}.png", "PNG")
            print(f"Image{count + 1} done")

    to_pdf(path_to_new)
    print("All done!")








