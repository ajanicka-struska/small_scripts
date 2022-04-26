from datetime import date
from time import time, sleep
import os
import pyscreenshot


folder_path = "C:\\Users\\ajanicka-struska\\Desktop\\"


def create_new_folder(folder_path):
    today = date.today()
    try:
        os.mkdir(folder_path + "screens-" + f"{today}")
    except FileExistsError:
        print("Folder already exists.")


def create_newlist():
    newlist = []
    for num in range(1, 10):
        name = "000" + str(num)
        newlist.append(name)
        num += 1
    for num in range(10, 100):
        name = "00" + str(num)
        newlist.append(name)
        num += 1
    for num in range(100, 301):
        name = "0" + str(num)
        newlist.append(name)
        num += 1
    print("List done!")
    return newlist


if __name__ == "__main__":
    list_of_numbers = create_newlist()
    create_new_folder(folder_path)
    folder_today = folder_path + "screens-" + str(date.today()) + "\\"

    start_time = time()
    for num in list_of_numbers:
        im = pyscreenshot.grab()
        im.save(folder_today + f"{num}.png")
        print(f"Screen {num} done!")
        sleep(60.0 - (time() - start_time) % 60.0)


