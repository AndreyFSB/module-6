import sys
from os import listdir
from os.path import isfile, join, isdir
from is_valid import is_valid
import glob


def main():
    path = sys.argv[1]
    if isdir(path):
        files = glob.glob(join(path, "*.txt"))
    else:
        files = [path]
    for file_ in files:
        with open(file_) as f:
            message = "Валидно" if is_valid(f.read()) else "Ошибка"
            print(f"{file_}: {message}")


if __name__ == "__main__":
    main()
