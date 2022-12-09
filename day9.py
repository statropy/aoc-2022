#day9.py 2022
import unittest

def move(h, t):
    dx, dy = h[0]-t[0], h[1]-t[1]
    if abs(dx) == 2 or abs(dy) == 2:
        dx = (dx>0) - (dx<0)
        dy = (dy>0) - (dy<0)
        t = t[0]+dx, t[1]+dy
    return t

def run(lines, tail=1):
    visited = set()
    r = [(0,0)]*(tail+1)
    moves = {'R':(1,0), 'L':(-1,0), 'U':(0,1), 'D':(0,-1)}
    visited.add(r[-1])

    for line in lines:
        direction, steps = line[0], int(line[2:-1])
        for _ in range(steps):
            m = moves[direction]
            r[0] = r[0][0] + m[0], r[0][1] +m[1]
            for i in range(tail):
                r[i+1] = move(r[i], r[i+1])
            visited.add(r[-1])

    return len(visited)

def part1(lines):
    return run(lines)

def part2(lines):
    return run(lines, 9)

class TestDay9(unittest.TestCase):
    def test_1a(self):
        with open('./test9.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 13)

    def test_1(self):
        with open('./input9.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 6357)

    def test_2a(self):
        with open('./test9.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 1)

    def test_2b(self):
        with open('./test9b.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 36)

    def test_2(self):
        with open('./input9.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 2627)

if __name__ == '__main__':
    unittest.main()
