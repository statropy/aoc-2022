#day12.py 2022
import unittest

class Node(object):
    R = [(-1,0), (0,-1), (1,0), (0,1)]
    width = 0
    height = 0
    grid = {}

    def __init__(self, x, y, weight, value=None):
        self.x = x
        self.y = y
        self.weight = weight
        self.value = value
        self.visited = False

    def neighbors(self):
        for d in Node.R:
            d = self.x+d[0], self.y+d[1]
            n = Node.grid.get(d)
            if n and n.weight <= self.weight + 1:
                yield n

    def reset():
        for node in Node.grid.values():
            node.value = None
            node.visited = False

def populate(lines):
    S = None
    E = None
    allAs = []
    Node.height = len(lines)
    Node.width = len(lines[0].strip())
    Node.grid = {}
    Node.q = []
    for y,row in enumerate(lines):
        for x,val in enumerate(row.strip()):
            iss, ise = False, False
            if val == 'S':
                val = 'a'
                iss = True
            elif val == 'E':
                val = 'z'
                ise = True
            n = Node(x,y,ord(val)-ord('a'))
            Node.grid[(x,y)] = n
            if iss:
                S = n
            elif ise:
                E = n
            if n.weight == 0:
                allAs.append(n)
    return S, E, allAs

def search(root, E):
    root.value = 0
    q = [root]
    while len(q) > 0:
        current = q.pop(0)
        if current.visited:
            continue
        current.visited = True
        for n in current.neighbors():
            if n.value is None or n.value > current.value + 1:
                n.value = current.value + 1
            if not n.visited:
                q.append(n)
    depth = E.value
    Node.reset()
    return depth

def part1(lines):
    S, E, _ = populate(lines)
    return search(S, E)

def part2(lines):
    _, E, allAs = populate(lines)
    return min([x for x in [search(a,E) for a in allAs] if x is not None])

class TestDay12(unittest.TestCase):
    def test_1a(self):
        with open('./test12.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 31)

    def test_1(self):
        with open('./input12.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 412)

    def test_2a(self):
        with open('./test12.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 29)

    def test_2(self):
        with open('./input12.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 402)

if __name__ == '__main__':
    unittest.main()
