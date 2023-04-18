from multiprocessing import Pool, Process, Array, Value

def get_start_value(d,next,i):
    if next[i] == -1:
        d[i] = 0
    else:
        d[i] = 1

def get_distance(d,next,i):
    if next[i] != -1:
        d[i] += d[next[i]]
        next[i] = next[next[i]]

def get_distances(d, next):
    processes = []
    for i in range(len(d)):
        processes.append(Process(get_start_value(d,next,i)))

    for i in range(len(d)):
        processes[i].start()

    for i in range(len(d)):
        processes[i].join()

    while next[0] != -1:
        processes2 = []
        for i in range(len(d)):
            processes2.append(Process(get_distance(d, next, i)))

        for i in range(len(d)):
            processes2[i].start()

        for i in range(len(d)):
            processes2[i].join()

    return d


if __name__ == '__main__':

    array = [2,3,2,5,3,2,1]
    len_from_end = Array('i',[0,0,0,0,0,0,0])
    next = Array('i',[1,2,3,4,5,6,-1])

    print(get_distances(len_from_end,next)[:])