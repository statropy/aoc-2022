// day1.cpp
#include <gtest/gtest.h>
#include <string>
#include <fstream>
#include <numeric>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Day1 {
protected:
    std::vector<int> sums;

public:
    Day1(const char *file) {
        ifstream infile(file);
        string line;

        sums.push_back(0);
        while (getline(infile,line)) {
            if (line.size() == 0) {
                sums.push_back(0);
            } else {
                sums.back() += stoi(line);
            }
        }
        infile.close();
    }

    int part1() {
        return *max_element(sums.begin(), sums.end());
        // int max = INT_MIN;
        // for (int i : sums) {
        //     if (i > max) {
        //         max = i;
        //     }
        // }
        // return max;
    }

    int part2() {
        sort(sums.begin(), sums.end());
        int sum = 0;
        for (auto it = sums.end()-3; it != sums.end(); it++) {
            sum += *it;
        }
        return sum;
    }
};

TEST(Day1, Part1_test) {
    ASSERT_EQ(Day1("../test1.txt").part1(), 24000);
}

TEST(Day1, Part1) {
    ASSERT_EQ(Day1("../input1.txt").part1(), 64929);
}

TEST(Day1, Part2_test) {
    ASSERT_EQ(Day1("../test1.txt").part2(), 45000);
}

TEST(Day1, Part2) {
    ASSERT_EQ(Day1("../input1.txt").part2(), 193697);
}
