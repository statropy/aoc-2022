#day5.py 2022
import unittest

def populate_stacks(lines):
    numstacks = len(lines[0]) // 4
    stacks = {}
    for i in range(numstacks):
        stacks[i+1] = []

    offset = 0
    for line in lines:
        offset += 1
        if line[1] == '1':
            break
        for i in range(numstacks):
            c = line[(i*4)+1]
            if c != ' ':
                stacks[i+1].append(c)

    for i in range(numstacks):
        stacks[i+1].reverse()

    return lines[offset+1:], stacks

def part1(lines):
    lines, stacks = populate_stacks(lines)

    for line in lines:
        numtomove, src, dst = [int(x) for x in line.split() if x[0].isdigit()]
        for _ in range(numtomove):
            z = stacks[src].pop()
            stacks[dst].append(z)
    return ''.join([stacks[z+1][-1] for z in range(len(stacks))])

def part2(lines):
    lines, stacks = populate_stacks(lines)

    for line in lines:
        numtomove, src, dst = [int(x) for x in line.split() if x[0].isdigit()]
        stacks[src], moving = stacks[src][:-numtomove], stacks[src][-numtomove:]
        stacks[dst] += moving
    return ''.join([stacks[z+1][-1] for z in range(len(stacks))])

class TestDay5(unittest.TestCase):
    def test_1a(self):
        with open('./test5.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 'CMZ')

    def test_1(self):
        with open('./input5.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 'TDCHVHJTG')

    def test_2a(self):
        with open('./test5.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 'MCD')

    def test_2(self):
        with open('./input5.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 'NGCMPJLHV')

if __name__ == '__main__':
    unittest.main()
