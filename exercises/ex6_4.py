#!/usr/bin/env python3


def sumall(*input_data):
    '''Viết function ``sumall`` tính tổng của tất cả các argument (int, float,
    hoặc string) được gọi. Thay input_data bằng code phù hợp.
    '''

    return sum([float(val) for val in input_data])
    pass


def solve():
    result = None

    result = sumall(1, 2, 3, 4.5, 5, ' 6 ')
    result2 = sumall(1, 2, 3, 4.5, 5, 9, ' 6 ')

    return result, result2


def main():
    print(solve())


if __name__ == "__main__":
    main()
