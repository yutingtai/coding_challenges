if __name__ == '__main__':
    A=[]
    B=[]
    for _ in range(1):
        cordinate_A = input().split()
        cordinate_B = input().split()
        for i in cordinate_A:
            A.append(int(i))
        for i in cordinate_B:
            B.append(int(i))

cartesian =[(x, y) for x in A for y in B]
for cor in cartesian:
    print(cor,end=" ")
