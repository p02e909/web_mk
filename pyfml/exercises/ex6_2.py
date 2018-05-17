#!/usr/bin/env python3


def chunk_a_list(iterable, N):
    return list(zip(*[iter(iterable)]*N))


def solve(iterable, N):
    ''' Chia input_data thành các tuple chứa N phần tử (chunk a list).
    Nếu tuple cuối không đủ phần tử thì bỏ đi.
    '''
    result = None
    # sửa thành tên function phù hợp
    result = chunk_a_list(iterable, N)

    return result


def main():
    li = ['meo', 'bo', 'ga', 'cho', 'chim', 'gau', 'voi']
    print(solve(li, 2))


if __name__ == "__main__":
    main()
