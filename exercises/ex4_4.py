#!/usr/bin/env python3


def solve():
    '''Tính số nghiệm của bài toán lớp 3

    Với các biến a,b,c,d,e,f,g,h,i là các số nằm trong khoảng 1-9 (các biến có
    thể có giá trị giống nhau), dạng biểu thức:

      a + 13 * b / c + d + 12 * e – f – 11 + g * h / i – 10 = 66

    Bài toán lớp 3 có số đáp án khổng lồ
    (http://www.familug.org/2015/05/codegolf-giai-bai-toan-lop-3-co-so.html)
    '''

    result = None

    count = 0
    for b in range(1,10):
        for g in range(1,10):
            for h in range(1,10):
                for c in range(1,10):
                    for i in range(1,10):
                        bien1 = 13*b*i+g*h*c
                        bien2 = c*i
                        for f in range(1,10):
                            for e in range(1,10):
                                for a in range(1,10):
                                    for d in range(1,10):
                                        bien3 = bien2*(87+f-12*e-1 -d)
                                        if bien1 == bien3:
                                            count = count + 1
                                            

    result = count
    return result


def main():
    print(solve())


if __name__ == "__main__":
    main()
