import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':
    filenames = [f'./file_{number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.time() - start_time
    print(f"Линейный вызов: {linear_duration:.6f} секунд")

    # Многопроцессный вызов
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    parallel_duration = time.time() - start_time
    print(f"Многопроцессный вызов: {parallel_duration:.6f} секунд")
