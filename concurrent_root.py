import ctypes
from multiprocessing import Pool, Process, Array, Value
iterations = 0
class Node:
    parent = None
    root = None

    def __init__(self, parent=None):
        self.parent = parent
        self.root = None

# To można zrobić współbieżnie też
def exists_without_parent(nodes):
    for node in nodes:
        if node.parent is None:
            return True
    return False


def findRootStep(node_arr, idx):
    if node_arr[idx].parent is not None:
        node_arr[idx].root = node_arr[idx].parent.root
        node_arr[idx].parent = node_arr[idx].parent.parent

def findRoots(nodes):
    while exists_without_parent(nodes):
        global iterations
        iterations += 1
        if iterations > 100:
            exit(1)
        pool = Pool(len(nodes))
        pool.map(findRootStep, nodes)
        for i in range(len(nodes)):
            findRootStep(nodes, i)
    return nodes
if __name__ == "__main__":
    n = int(7)
    nodes = [Node() for i in range(n)]
    nodes[0].root = nodes[0]
    nodes[1].parent = nodes[0]
    nodes[2].parent = nodes[1]
    nodes[3].parent = nodes[1]
    nodes[4].parent = nodes[2]
    nodes[5].parent = nodes[2]
    nodes[6].parent = nodes[0]
    nodes = findRoots(Array('f', nodes))
    for node in nodes:
        print("Node: ", node, "Parent: ", node.parent, "Root: ", node.root)