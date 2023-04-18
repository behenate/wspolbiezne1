from random import randint, seed
from multiprocessing import Process, Array


def partition(tab, p, r):
    last = tab[r]
    i = p - 1
    for j in range(p, r):
        if tab[j] <= last:
            i = i + 1
            tab[i], tab[j] = tab[j], tab[i]

    tab[i + 1], tab[r] = tab[r], tab[i + 1]
    return i + 1


def quicksort(tab, p, r):
    if p < r:
        i = partition(tab, p, r)
        p1 = Process(target=quicksort, args=(tab, p, i - 1))
        p2 = Process(target=quicksort, args=(tab, i + 1, r))
        p1.start()
        p2.start()
        p1.join()
        p2.join()


if __name__ == "__main__":
    n = 10
    seed(420)
    T = Array('i', [randint(1, n) for i in range(n)])
    quicksort(T, 0, len(T) - 1)
    print(T[:])

