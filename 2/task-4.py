import sys
import random
import string
import asyncio
import multiprocessing
from concurrent.futures import ProcessPoolExecutor

CPU_COUNT = multiprocessing.cpu_count()

executor = ProcessPoolExecutor(max_workers=CPU_COUNT)
loop = asyncio.get_event_loop()
chars = string.digits + string.ascii_uppercase + string.ascii_lowercase


def create_random_strings(number: int) -> list:  # worker
    result = []
    for _ in range(number):
        line_len = random.randint(2, 50)
        line = random.sample(chars, line_len) + random.sample(chars, line_len) + ["\n"]
        result.append("".join(line))
    return result


async def create_coro(num: int):
    return await loop.run_in_executor(executor, create_random_strings, num)


def main():
    file_name = sys.argv[1]
    strings_number = int(sys.argv[2])

    with open(file_name, "w+") as f:
        tasks = [
            asyncio.ensure_future(create_coro(strings_number // CPU_COUNT))
            for _ in range(CPU_COUNT)
        ]
        for l in loop.run_until_complete(asyncio.gather(*tasks)):
            for s in l:
                f.write(s)


if __name__ == "__main__":
    main()
