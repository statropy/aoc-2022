#day7.py 2022
import unittest

class Node(object):

    def __init__(self, name='/', parent=None):
        self.subdirs = {}
        self.files = {}
        self.name = name
        self.parent = parent
        self.dirsize = None

    def __repr__(self):
        if self.parent:
            return repr(self.parent) + self.name + '/'
        return self.name

    def add_dir(self, dir):
        self.subdirs[dir] = Node(dir, self)

    def add_file(self, file, size):
        self.files[file] = size

    def size(self):
        if self.dirsize is None:
            self.dirsize = sum(self.files.values()) + sum([d.size() for d in self.subdirs.values()])
        return self.dirsize

    def allsubdirs(self):
        for node in self.subdirs.values():
            yield from node.allsubdirs()
            yield node

def makefs(lines):
    root = Node()
    cwd = root
    for line in lines:
        if line[:4] == '$ cd':
            dir = line[5:-1]
            if dir == '/':
                cwd = root
            elif dir == '..':
                cwd = cwd.parent
            else:
                cwd = cwd.subdirs[dir]
        elif line[:4] == '$ ls':
            pass
        elif line[:3] == 'dir':
            dir = line[4:-1]
            cwd.add_dir(dir)
        else:
            size, file = line.strip().split(' ')
            cwd.add_file(file, int(size))
    return root

def part1(lines):
    return sum([d.size() for d in makefs(lines).allsubdirs() if d.size() <= 100000])

def part2(lines):
    root = makefs(lines)
    unused = 70000000 - root.size()
    todel = 30000000 - unused
    return min([d.size() for d in root.allsubdirs() if d.size() > todel])

class TestDay7(unittest.TestCase):
    def test_1a(self):
        with open('./test7.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 95437)

    def test_1(self):
        with open('./input7.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 1427048)

    def test_2a(self):
        with open('./test7.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 24933642)

    def test_2(self):
        with open('./input7.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 2940614)

if __name__ == '__main__':
    unittest.main()
