#day14.py 2022
import unittest

def add_point(cave, pos):
    x, y = pos
    s = cave.setdefault(x, [])
    s.append(y)
    s.sort()

def make_cave(lines):
    cave = {}
    maxy = 0
    for line in lines:
        segments = line.strip().split(' -> ')
        pos = None
        for segment in segments:
            x, y = [int(z) for z in segment.split(',')]
            if pos is None:
                pos = x,y
                maxy = max(maxy, y)
                add_point(cave, pos)
            else:
                move = (1,0)
                steps = abs(pos[0]-x)
                if x == pos[0]:
                    steps = abs(pos[1]-y)
                    if y < pos[1]:
                        move = (0, -1)
                    else:
                        move = (0, 1)
                elif x < pos[0]:
                    move = (-1, 0)
                
                for _ in range(steps):
                    pos = pos[0]+move[0], pos[1]+move[1]
                    maxy = max(maxy, pos[1])
                    add_point(cave, pos)
    return cave, maxy+2

def find_next(rows, y):
    z = sorted(rows + [y])
    if z[-1] == y:
        return None #nothing below
    return z[z.index(y)+1]-1

def move(cave):
    x, y = 500, 0
    while True:
        try:
            y = find_next(cave[x], y)
            if y is None:
                return True

            if y+1 not in cave[x-1]:
                x, y = x-1, y+1
                continue
            if y+1 not in cave[x+1]:
                x, y = x+1, y+1
                continue
            add_point(cave, (x,y))
            return False
        except KeyError:
            return True

def find_next2(rows, y):
    z = sorted(rows + [y])
    return z[z.index(y)+1]-1

def move2(cave, bottom):
    x, y = 500, 0
    while True:
        y = find_next2(cave.setdefault(x, [bottom]), y)
        if y is None:
            return True

        if y+1 not in cave.setdefault(x-1, [bottom]):
            x, y = x-1, y+1
            continue
        
        if y+1 not in cave.setdefault(x+1, [bottom]):
            x, y = x+1, y+1
            continue
        add_point(cave, (x,y))
        return x == 500 and y == 0

def part1(lines):
    cave, _ = make_cave(lines)
    grains = 0
    while True:
        if move(cave):
            break
        grains += 1

    return grains

def part2(lines):
    cave, bottom = make_cave(lines)
    for y in cave.values():
        y.append(bottom)
    grains = 0
    while True:
        grains += 1
        if move2(cave, bottom):
            break

    return grains

class TestDay14(unittest.TestCase):
    def test_1a(self):
        with open('./test14.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 24)

    def test_1(self):
        with open('./input14.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 618)

    def test_2a(self):
        with open('./test14.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 93)

    def test_2(self):
        with open('./input14.txt', 'r') as f:
            self.assertEqual(part2(list(f)), None)

if __name__ == '__main__':
    unittest.main()
