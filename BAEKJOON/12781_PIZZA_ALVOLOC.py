import sys
input = sys.stdin.readline


def ccw(x1, y1, x2, y2, x3, y3):
    return x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3


def is_cross(x1, y1, x2, y2, x3, y3, x4, y4):
    ccw1 = ccw(x1, y1, x2, y2, x3, y3)
    ccw2 = ccw(x1, y1, x2, y2, x4, y4)

    if ccw1 >= 0 and ccw2 >= 0: return 0
    if ccw1 <= 0 and ccw2 <= 0: return 0

    return 1


x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
print(is_cross(x1, y1, x2, y2, x3, y3, x4, y4))