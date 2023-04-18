from math import inf
from random import randint, seed
from multiprocessing import Process, Array, Pipe


def merge(tab, p, q, r):
    left = tab[p:q + 1]
    right = tab[q + 1:r + 1]
    # Dodanie wartownika na koniec listy
    left.append(inf)
    right.append(inf)
    i = 0
    j = 0
    for k in range(p, r + 1):
        if left[i] <= right[j]:
            tab[k] = left[i]
            i += 1
        else:
            tab[k] = right[j]
            j += 1
    return tab

def merge_sort(tab, p, r):
    if p < r:
        q = (p + r) // 2
        p1 = Process(target=merge_sort, args=(tab, p, q))
        p2 = Process(target=merge_sort, args=(tab, q + 1, r))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        merge(tab, p, q, r)

def merge_sort_pipes(tab, p, r, result_conn):
    if p < r:
        parent_conn, child_conn = Pipe()
        parent_conn2, child_conn2 = Pipe()
        q = (p + r) // 2

        p1 = Process(target=merge_sort_pipes, args=(tab, p, q, child_conn))
        p2 = Process(target=merge_sort_pipes, args=(tab, q + 1, r, child_conn2))
        p1.start()
        p2.start()
        m1 = parent_conn.recv()
        m2 = parent_conn2.recv()
        p1.join()
        p2.join()
        rr = m1[:q+1] + m2[q+1:]
        tab = merge(rr, p, q, r)
        result_conn.send(tab)
    else:
        result_conn.send(tab)



seed(100)
a = [randint(0, 100) for _ in range(100000)]
shared_a = Array('i', a)
print(a)
p_conn, c_conn = Pipe()
process = Process(target=merge_sort_pipes, args=(a, 0, len(a) - 1, c_conn))
process.start()
print(p_conn.recv())
process.join()