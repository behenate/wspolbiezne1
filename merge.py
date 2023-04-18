from multiprocessing import Process, Array, Value
from math import inf


def binary_search(arr, num):
    left = 0
    right = len(arr) - 1
    while left <= right:
        m = (left + right) // 2
        if num < arr[m]:
            right = m - 1
        elif num > arr[m]:
            left = m + 1
        else:
            print(m)
            return m
    print(arr[max(left, right)])
    return max(left, right)


iterations = 0


def merge(left, right, i, j, k, l, p, q, result):
    m = j - i
    n = l - k
    if m < n:
        tmp = left[:]
        m = n
        i_tmp = i
        j_tmp = j
        i = k
        j = l
        k = i_tmp
        l = j_tmp

        left = right[:]
        right = tmp[:]
    if m == 0:
        return
    r = (i + j) // 2
    s = binary_search(right, left[r])
    t = p + r - i + s - k
    result[t] = left[r]
    global iterations
    iterations += 1
    if iterations > 100:
        exit(1)
    p1 = Process(target=merge, args=(left, right, i, r, k, s, p, t, result))
    p2 = Process(target=merge, args=(left, right, r + 1, j, s, l, t + 1, q, result))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == "__main__":
    left = [1, 3, 5, 7, 9,123,234324, inf]
    right = [2, 4, 6, 8, 10,123123,1231231232,inf]
    result = Array('i', [0] * (len(left)+len(right)-2))
    print(result[:])
    merge(left, right, 0, len(left)-1, 0, len(right)-1, 0, len(left)+len(right), result)
    print(result[:])
