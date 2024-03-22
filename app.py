import math
import sys
from threading import Thread

import numpy as np


def _main(threads_count: int | None) -> None:
    numbers_count = 10_000_000_000
    arr = np.ones(numbers_count, dtype=np.int8)

    if threads_count is None:
        _calc(arr)
    else:
        _calc_threads(arr, threads_count)


def _calc(arr: np.ndarray) -> None:
    sum = arr.sum()
    print(sum)


def _calc_threads(arr: np.ndarray, threads_count: int) -> None:
    res_arr = np.zeros(threads_count, np.int_)

    threads: list[Thread] = []
    thread_numbers_count: int = math.ceil(len(arr) / threads_count)
    current_number_index: int = 0
    for i in range(threads_count):
        thread = Thread(target=_worker, args=[arr[current_number_index:current_number_index+thread_numbers_count], res_arr, i])
        threads.append(thread)
        thread.start()
        current_number_index += thread_numbers_count

    for thread in threads:
        thread.join()

    res_sum = res_arr.sum()
    print(res_sum)


def _worker(arr: np.ndarray, res_arr: np.ndarray, res_index: int) -> None:
    res_arr[res_index] = arr.sum()


if __name__ == '__main__':
    threads_count: int | None = int(sys.argv[1]) if len(sys.argv) == 2 else None
    _main(threads_count)
