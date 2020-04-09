# start 11:26 end 12:00
# start 13:56
# лице по херонова формула
# ако лицето е квадрат от периментъра значи са подобни
import math
from typing import List, Tuple
Coords = List[Tuple[int, int]]

def Tr_perimeter(a, b, c):
    return a + b + c
def Tr_lice(a, b, c):
    pass
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))
def similar_triangles(coords_1: Coords, coords_2: Coords) -> bool:
    a = round(math.sqrt(pow(abs(coords_1[0][0] - coords_1[1][0]), 2) + pow(abs(coords_1[0][1] - coords_1[1][1]), 2)), 6)
    b = round(math.sqrt(pow(abs(coords_1[1][0] - coords_1[2][0]), 2) + pow(abs(coords_1[1][1] - coords_1[2][1]), 2)), 6)
    c = round(math.sqrt(pow(abs(coords_1[2][0] - coords_1[0][0]), 2) + pow(abs(coords_1[2][1] - coords_1[0][1]), 2)), 6)
    print(a, b, c)
    # strani na vtori triagalnik
    A = round(math.sqrt(pow(abs(coords_2[0][0] - coords_2[1][0]), 2) + pow(abs(coords_2[0][1] - coords_2[1][1]), 2)), 6)
    B = round(math.sqrt(pow(abs(coords_2[1][0] - coords_2[2][0]), 2) + pow(abs(coords_2[1][1] - coords_2[2][1]), 2)), 6)
    C = round(math.sqrt(pow(abs(coords_2[2][0] - coords_2[0][0]), 2) + pow(abs(coords_2[2][1] - coords_2[0][1]), 2)), 6)
    print(A, B, C)
     # your code here
    k = round((Tr_perimeter(a, b, c) / Tr_perimeter(A, B, C)), 6)
    K = round((Tr_lice(a, b, c) / Tr_lice(A, B, C)), 6)
    print(round(k, 6), round(K, 6))
    if K == round(pow(k, 2), 6):
        return True
    else:
        return False



if __name__ == '__main__':
    print("Example:")
    print(similar_triangles([[2,-3],[1,-5],[2,-1]],[[0,7],[6,4],[-6,7]]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 2), (5, 0)]) is True, 'basic'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(3, 0), (4, 3), (5, 0)]) is False, 'different #1'
    assert similar_triangles([(0, 0), (1, 2), (2, 0)], [(2, 0), (4, 4), (6, 0)]) is True, 'scaling'
    assert similar_triangles([(0, 0), (0, 3), (2, 0)], [(3, 0), (5, 3), (5, 0)]) is True, 'reflection'
    assert similar_triangles([(1, 0), (1, 2), (2, 0)], [(3, 0), (5, 4), (5, 0)]) is True, 'scaling and reflection'
    assert similar_triangles([(1, 0), (1, 3), (2, 0)], [(3, 0), (5, 5), (5, 0)]) is False, 'different #2'
    print("Coding complete? Click 'Check' to earn cool rewards!")
