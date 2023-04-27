# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


def find_angle_theta(ab, bc):
    ac = math.sqrt(ab ** 2 + bc ** 2)
    mc = math.sqrt(ab ** 2 + bc ** 2)/2
    angle_c_rad = math.asin(ab/ac)
    bm = math.sqrt(bc**2+mc**2-2*bc*mc*math.cos(angle_c_rad))
    theta = round(math.asin(ac*math.sin(angle_c_rad)/(2*bm))*57.296)
    print(f'{theta}'+chr(176))


if __name__ == '__main__':
    for _ in range(1):
        ab = int(input())
        bc = int(input())
    find_angle_theta(ab,bc)

