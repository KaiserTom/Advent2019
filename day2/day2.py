import math
import sys
import os
import ast

def opcode1(x, y, intcode):
    return intcode[x] + intcode[y]


def opcode2(x, y, intcode):
    return intcode[x] * intcode[y]


def intcode_computer(intcode):
    x = 0
    y = 0
    switch = {
        1 : opcode1,
        2 : opcode2
    }

    i = 0
    code = intcode[i]
    while code != 99:
        x = intcode[i + 1]
        y = intcode[i + 2]
        z = intcode[i + 3]
        result = switch[code](x, y, intcode)
        intcode[z] = result
        i = i + 4
        code = intcode[i]
    
    return intcode[0]

def find_nounverb(intcode):
    intcode2 = list(intcode)
    for noun in range(100):
        for verb in range(100):
            intcode2[1], intcode2[2] = noun, verb
            result = intcode_computer(intcode2)
            if result == 19690720:
                return noun, verb
            else:
                intcode2 = list(intcode)



def load_inputs():
    intcode = []
    with open("day2input.txt", "r") as file:
        intcode = ast.literal_eval(file.read())

    return intcode


def main():
    intcode = load_inputs()
    result = find_nounverb(intcode)
    answer = 100 * result[0] + result[1]
    print(result, answer)

main()