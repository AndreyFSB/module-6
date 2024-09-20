#!/usr/bin/python3

import sys
import random
import string

chars = string.digits + string.ascii_uppercase + string.ascii_lowercase


def get_random_string() -> str:
    line_len = random.randint(2, 50)
    line = "".join(random.sample(chars, line_len))
    line += "".join(random.sample(chars, line_len)) + "\n"
    return line


def main():
    file_name = sys.argv[1]
    strings_number = int(sys.argv[2])
    lines = []

    for i in range(0, strings_number):
        lines.append(get_random_string())

    with open(file_name, "w") as f:
        f.writelines(lines)


if __name__ == "__main__":
    main()
