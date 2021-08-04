import os
from PIL import Image
from fpdf import FPDF

def get_path():
    return (input("Write path to folder here:\n")).replace("\"", "") + "\\"


def create_newfolder(p):
    try:
        os.mkdir(p + "new")
        print("New folder done!")
        return p + "new"
    except FileExistsError:
        print("Path already exists!")
        return p + "new"


def read_files(old_path):
    list_of_files = os.listdir(old_path)
    return [l for l in list_of_files if os.path.isfile(os.path.join(old_path, l))]


def crop_dimensions():
    left = int(input("Left dimension:\n"))
    upper = int(input("Upper dimension:\n"))
    right = int(input("Right dimension:\n"))
    lower = int(input("Lower dimension:\n"))
    return left, upper, right, lower


if __name__ == "__main__":
    path = get_path()
    create_newfolder(path)
    path_to_new = path + "new\\"
    list_of_images = read_files(path)
    dimensions = tuple(crop_dimensions())

    for count, value in enumerate(list_of_images):
        image = Image.open(path + "\\" + value)
        image_cropped = image.crop(dimensions)
        if count < 10:
            image_cropped.save(path_to_new + "\\000" + str(count + 1) + ".png", "PNG")
            print("Image " + str(count + 1) + " done")
        elif 10 <= count <= 99:
            image_cropped.save(path_to_new + "\\00" + str(count + 1) + ".png", "PNG")
            print("Image " + str(count + 1) + " done")
        elif 100 <= count <= 999:
            print("Image " + str(count + 1) + " done")
            image_cropped.save(path_to_new + "\\0" + str(count + 1) + ".png", "PNG")
        else:
            image_cropped.save(path_to_new + "\\" + str(count + 1) + ".png", "PNG")
            print("Image " + str(count + 1) + " done")

    pdf = FPDF("P", "mm", "A4")

    new_list_of_images = read_files(path_to_new)

    for elem in new_list_of_images:
        pdf.add_page()
        pdf.image(path_to_new + elem, 0, 0, 210, 297)

    pdf.output(path_to_new + "new_book.pdf", "F")

    print("All done!")








