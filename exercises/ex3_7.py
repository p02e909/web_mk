#!/usr/bin/env python3

'''
Xét các số nguyên dương < 100, in ra các số chia hết cho 5 theo dạng::

    5 == 1 * 5
    10 == 2 * 5
    15 == 3 * 5
    ...
'''

result=[]
def solve():
    '''Trả về 1 `list` các `string` có dạng:

        output: ['5 = 1 * 5', '10 = 2 * 5', ...]

    Lưu ý: Thứ tự tăng dần theo bảng cửu chương
    '''

    fmt = '{0} = {1} * 5'
        
    for i in (range(1,100)):
        if i % 5 == 0:
            result.append(fmt.format(i, i//5))
    return result

def main():
    # for i in solve():
    #      print(i)
    solve()
    print(result)
   

if __name__ == "__main__":
    main()
