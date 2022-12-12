#day11.py 2022
import unittest

class Monkey(object):

    modulo = 1

    def __init__(self, m, items, left, op, right, divisible, t, f, div=None):
        self.m = m
        self.items = items
        self.left = left
        self.op = op
        self.right = right
        self.divisible = divisible
        self.t = t
        self.f = f
        self.inspect = 0
        self.div = div

    def __repr__(self):
        return '{} {} {}{}{} /{} {} {}'.format(self.m, self.items, self.left, self.op, self.right, self.divisible, self.t, self.f)

    def operation(self, item):
        self.inspect += 1
        left, right = item, item
        if self.left != 'old':
            left = int(self.left)
        if self.right != 'old':
            right = int(self.right)

        if self.op == '+':
            a = (left + right)
        else:
            a = (left * right)

        a %= Monkey.modulo
        
        if self.div is not None:
            a //= 3
        return a

    def test(self, item):
        if item % self.divisible == 0:
            return self.t
        return self.f

    def push(self, item):
        self.items.append(item)

    def parse(text, div=None):
        if text[0] == '\n':
            text.pop(0)
        m = int(text[0].split(':')[0].split()[1])
        items = [int(item.strip()) for item in (text[1].split(':')[1]).split(',')]
        left, op, right = text[2].strip().split('=')[1].split()
        test = int(text[3].strip().split()[-1])
        t = int(text[4].strip().split()[-1])
        f = int(text[5].strip().split()[-1])
        return Monkey(m, items, left, op, right, test, t, f, div), text[6:]

    def parseall(text, div=None):
        monkeys = []
        while text:
            m, text = Monkey.parse(text, div)
            monkeys.append(m)
        for m in monkeys:
            Monkey.modulo *= m.divisible
        return monkeys

    def round(monkeys):
        for monkey in monkeys:
            for item in monkey.items:
                newitem = monkey.operation(item)
                newmonkey = monkey.test(newitem)
                monkeys[newmonkey].push(newitem)
            monkey.items = []

def part1(lines):
    monkeys = Monkey.parseall(lines, 3)
    for _ in range(20):
        Monkey.round(monkeys)
    inspected = sorted([m.inspect for m in monkeys])
    return inspected[-1] * inspected[-2]

def part2(lines):
    monkeys = Monkey.parseall(lines)
    for round in range(10000):
        Monkey.round(monkeys)
    inspected = sorted([m.inspect for m in monkeys])
    return inspected[-1] * inspected[-2]

class TestDay11(unittest.TestCase):
    def test_1a(self):
        with open('./test11.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 10605)

    def test_1(self):
        with open('./input11.txt', 'r') as f:
            self.assertEqual(part1(list(f)), 54054)

    def test_2a(self):
        with open('./test11.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 2713310158)

    def test_2(self):
        with open('./input11.txt', 'r') as f:
            self.assertEqual(part2(list(f)), 14314925001)

if __name__ == '__main__':
    unittest.main()
