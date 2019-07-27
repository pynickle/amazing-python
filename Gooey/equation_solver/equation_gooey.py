import math
import re
import sys
import argparse
from gooey import Gooey


@Gooey(program_name="equation solver")
def main():
    parser = argparse.ArgumentParser(description="solve the maths equation")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-q", "--quadratic", help="enter the quadratic equation")
    group.add_argument("-d", "--dimensional", help="enter the one-dimensional equation")
    abc = parser.add_subparsers(help="subparsers")
    abc_parser = abc.add_parser("abc", help = "use abc template")
    group2 = abc_parser.add_mutually_exclusive_group()
    group2.add_argument("-aq", "--quadratic", help="enter the quadratic equation", nargs = 3)
    group2.add_argument("-ad", "--dimensional", help="enter the one-dimensional equation", nargs = 2)
    args = parser.parse_args()
    # print(args.equation)
    print(args)
    if args.quadratic:
        if isinstance(args.quadratic, list):
            solve_abc_quadratic_equation(args.quadratic)
        else:
            solve_quadratic_equation(args.quadratic)
    if args.dimensional:
        if isinstance(args.dimensional, list):
            solve_abc_dimensional_equation(args.dimensional)
        else:
            solve_dimensional_equation(args.dimensional)


def judge(a):
    if a > 0:
        return "+ " + str(a)
    if a == 0:
        return "+ "
    if a < 0:
        return "- " + str(-a)


def judge_first(a):
    if a == "":
        return "1"
    else:
        return a

def solve_abc_quadratic_equation(lst):
    solve_quadratic(lst[0], lst[1], lst[2])

def solve_abc_dimensional_equation(lst):
    solve_dimensional(lst[0], lst[1])

def solve_quadratic(a, b, c):
    a, b, c = int(a), int(b), int(c)
    delta = b ** 2 - 4 * a * c

    print("方程：" + judge(a) + "x^2 " + judge(b) + "x " + judge(c))

    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / a
        x2 = (-b - math.sqrt(delta)) / a
        print("x1 = " + str(x1))
        print("x2 = " + str(x2))
    elif delta == 0:
        x = -b / a
        print("x1 = x2 = " + str(x))
    else:
        print("无实数解！")

def solve_dimensional(a, b):
    a, b = int(a), int(b)
    print("方程：" + judge(a) + "x " + judge(b))
    if a == 0:
        print("x为任意实数")
    else:
        x = -b / a
        print("x = " + str(x))

def solve_quadratic_equation(sentence):
    pattern = r"([+-]?)(\d*)x\^2[ ]?([+-])[ ]?(\d+*)x[ ]?([+-])[ ]?(\d+)"
    # print(pattern)

    res = re.match(pattern, sentence)
    # print(res.groups())
    if not res:
        print("方程不合法")
        sys.exit()
    else:
        g2 = judge_first(res.group(2))
        g4 = judge_first(res.group(4))
        g6 = judge_first(res.group(6))
        a = int(res.group(1) + g2)
        b = int(res.group(3) + g4)
        c = int(res.group(5) + g6)
    solve_quadratic(a, b, c)

def solve_dimensional_equation(sentence):
    # pattern = r"([+-]?)([\d+]?)x[ ]?([+-])[ ]?(\d+)"
    pattern = r"([+-]?)(\d*)x[ ]?([+-])[ ]?(\d+)"
    res = re.match(pattern, sentence)
    if not res:
        print("方程不合法")
        sys.exit()
    else:
        g2 = judge_first(res.group(2))
        g4 = judge_first(res.group(4))
        a = int(res.group(1) + g2)
        b = int(res.group(3) + g4)
    solve_dimensional(a, b)

if __name__ == "__main__":
    main()
