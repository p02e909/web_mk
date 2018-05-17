#!/usr/bin/env python3

import random
def solve(N):
    '''
    Giả lập việc một người tiến lên hoặc lùi lại, biết ta có thể
    giả lập việc người này tiến hay lùi bằng:

    random.choice(True, False) # nếu quy ước True là tiến, False là lùi.

    Với N trường hợp, tính tỷ lệ người này tiến lên
    phía trước với mỗi trường hợp.

    Trường hợp 1: chỉ bước 1 bước
    Trường hợp 2: bước 2 bước
    ...
    Trường hợp N: bước N bước

    Output là list tỷ lệ người này tiến lên phía trước trong
    N trường hợp (ở dạng float, vd 50% là 0.5).

    Đối với học viên học data analysis, yêu cầu sử dụng thư viện numpy để làm.
    '''
    result = None
    buoc_tien = 0
    for so_buoc in range(1, N+1):
        if random.choice([True, False]) == True:
            buoc_tien = buoc_tien + 1
    result = buoc_tien/N  
    return result


def main():
    print(solve(100))


if __name__ == "__main__":
    main()
