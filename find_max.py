from multiprocessing import Pool

# Press the green button in the gutter to run the script.
T = [123123123123, 1, 2, 3, 4, 5, 6, 8, 7, 6,123, 5, 4, 3,5,12312342]

results = T[:]


def greater(arr):
    if len(arr) == 1:
        return arr[0]
    if arr[0] > arr[1]:
        return arr[0]
    else:
        return arr[1]


if __name__ == '__main__':
    pool = Pool(len(T) // 2 + 1)
    while len(results) > 1:
        n = len(results)
        results = pool.map(greater, [[results[i], results[i + 1] if i != n-1 else results[i]] for i in range(0, n, 2)])
        print(results)