from multiprocessing import Process, Pool, Value

# Press the green button in the gutter to run the script.
T = [5] * 1000

results = T[:]
def add_nums(arr, idx, sum_val):
    sum_val.value += arr[idx]
    return sum_val.value


if __name__ == '__main__':
    sum_val = Value('i', 0)
    pool = Pool(len(T))
    args = []
    processes = []
    for i in range(len(T)):
        processes.append(Process(target=add_nums, args= (T, i, sum_val)))
        processes[i].start()
    for i in range(len(T)):
        processes[i].join()
    print(sum_val.value)