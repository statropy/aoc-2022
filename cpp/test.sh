#!/bin/zsh
echo "Testing C++ Day $1"
g++ -o test_build/day$1 day$1.cpp -Ltest_build -lgtest -lgtest_main -pthread -std=c++0x && test_build/day$1
