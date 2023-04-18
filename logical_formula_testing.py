from multiprocessing import Process, Array, Queue, Value

FORMULA_SIZE = 5
# very complicated, which has 23 variables and returns true only in two cases
def formula(x1,x2,x3,x4,x5):
    return [x1,x2,x3,x4,x5] == [1,0,1,0,1]




def check_satisfiability(inputs, currently_testing, q):
    print(currently_testing)
    q1 = Queue()
    q2 = Queue()
    inputs1 = inputs[:]
    inputs2 = inputs[:]
    inputs1[currently_testing] = 0
    inputs2[currently_testing] = 1

    if formula(*inputs1):
        print(inputs)
        q.put(True)

    if formula(*inputs2):
        print(inputs)
        q.put(True)

    if currently_testing + 1 < FORMULA_SIZE:
        p1 = Process(target=check_satisfiability, args=(inputs1, currently_testing + 1, q1))
        p2 = Process(target=check_satisfiability, args=(inputs2, currently_testing + 1, q2))

        p1.start()
        p2.start()
        p1.join()
        p2.join()

    if currently_testing + 1 < FORMULA_SIZE and q1.get():
        q.put(True)
    inputs[currently_testing] = 1

    if currently_testing + 1 < FORMULA_SIZE and q2.get():
        q.put(True)
    q.put(False)


if __name__ == "__main__":
    inputs = [False] * 5
    inputs_m = Array('i', inputs)
    queue = Queue()
    print(check_satisfiability(inputs_m, 0, queue))