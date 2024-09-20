import sys
from is_valid import is_valid


def main():
    file_name = sys.argv[1]
    with open(file_name) as f:
        if not is_valid(f.read()):
            print("Ошибка, скобки невалидны!")


if __name__ == "__main__":
    main()
