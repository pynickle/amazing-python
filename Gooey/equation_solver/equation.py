import math
import re
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="solve the quadratic equation")
    parser.add_argument("-e", "--equation", help="enter the quadratic equation")
    args = parser.parse_args()
    print(args.equation)
    solve_equation(args.equation)

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

def solve_equation(sentence):
    pattern = r"([+-]?)([\d+]?)x\^2[ ]?([+-])[ ]?([\d+]?)x[ ]?([+-])[ ]?(\d+)"
    # print(pattern)

    res = re.match(pattern, sentence)
    #print(res.groups())
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

    delta = b**2 - 4*a*c

    print("方程：" + judge(a) + "x^2 " + judge(b) + "x " + judge(c))

    if delta > 0:
        x1 = (-b + math.sqrt(delta))/a
        x2 = (-b - math.sqrt(delta))/a
        print("x1 = " + str(x1))
        print("x2 = " + str(x2))
    elif delta == 0:
        x = -b/a
        print("x1 = x2 = " + str(x))
    else:
        print("无实数解！")

if __name__ == "__main__":
    main()

