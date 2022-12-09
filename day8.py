#day8.py 2022
import unittest

def part1(grid):
    width = len(grid[0])
    height = len(grid)

    visible = (width * 2) + (height * 2) - 4

    for row in range(1,height-1):
        for col in range(1, width-1):
            t = grid[row][col]
            if t > max(grid[row][:col]) or \
               t > max(grid[row][col+1:]) or \
               t > max([grid[r][col] for r in range(row)]) or \
               t > max([grid[r][col] for r in range(row+1,height)]):
                visible += 1

    return visible

def part2(grid):
    width = len(grid[0])
    height = len(grid)

    score = 0

    for row in range(1,height-1):
        for col in range(1, width-1):
            l,r,u,d = col,width-1-col,row,height-1-row
            t = grid[row][col]

            #L
            for c,v in enumerate(reversed(grid[row][:col])):
                if v >= t:
                    l = c+1
                    break
            #R
            for c,v in enumerate(grid[row][col+1:]):
                if v >= t:
                    r = c+1
                    break
            #U
            for c,v in enumerate(reversed([grid[r][col] for r in range(row)])):
                if v >= t:
                    u = c+1
                    break
            #D
            for c,v in enumerate([grid[r][col] for r in range(row+1,height)]):
                if v >= t:
                    d = c+1
                    break
            score = max(score, r*l*u*d)
    return score

class TestDay8(unittest.TestCase):
    def test_1a(self):
        with open('./test8.txt', 'r') as f:
            self.assertEqual(part1([line.strip() for line in f]), 21)

    def test_1(self):
        with open('./input8.txt', 'r') as f:
            self.assertEqual(part1([line.strip() for line in f]), 1719)

    def test_2a(self):
        with open('./test8.txt', 'r') as f:
            self.assertEqual(part2([line.strip() for line in f]), 8)

    def test_2(self):
        with open('./input8.txt', 'r') as f:
            self.assertEqual(part2([line.strip() for line in f]), 590824)

if __name__ == '__main__':
    unittest.main()
