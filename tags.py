import os
import sys
import random


def read_previous_file():
    if os.path.isfile('previous.txt'):
        print("Previous document exists, reading it")
        with open('previous.txt', "r") as f:
            return f.read().replace(" ", "").split("#")
    else:
        print("No file exists, creating one")
        f = open("previous.txt", "x")
        return [""]


def write_to_previous_file(data):
    with open("previous.txt", "w") as f:
        f.write(data)
        f.close()


def write_on_phone(string_for_phone):
    words = string_for_phone.split(" ")
    for word in words:
        os.system(f'adb shell input text "\\{word}\\ "')


def pick_random(all_data):
    old_selections = read_previous_file()
    r_num = random.randrange(19, 30)
    print(f"Picking {r_num}.")
    selected = []
    for r in range(r_num):
        this_r = random.choice(all_data)
        while True:
            if this_r in selected: # or (this_r in old_selections):
                print("Matches the one we already have")
                this_r = this_r = random.choice(all_data)
            elif this_r in old_selections:
                print("Matches the one we had last time")
                this_r = this_r = random.choice(all_data)
            else:
                break
        selected.append(this_r)
    s = " #"
    s = "#" + s.join(selected)
    write_to_previous_file(s)
    return s


def load_hashes():
    with open("hashes.txt", "r") as f:
        data = f.read().replace("\n", "").replace(" ", "").split(",")
        print(f"Current list contains {len(data)} hashtags.")
        data_to_send = pick_random(data)
        print(data_to_send)
        # write_on_phone(data_to_send)


def main():
    load_hashes()


if __name__ == "__main__":
    main()
