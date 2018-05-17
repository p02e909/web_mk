#!/usr/bin/env python3

'''
- input_data = ["I", "Love", "You", "Chiu", "Chiu"]

- output: in ra thành cặp

Ví dụ::

  1 I
  2 Love
  3 You
  ... cho đến hết

Gợi ý: có thể dùng enumerate()
https://docs.python.org/2/library/functions.html#enumerate
'''


data = ["I", "Love", "You", "Chiu", "Chiu"]


def solve(input_data):
    '''Trả về 1 `list` các `tuple` theo định dạng sau:

        result = [(1, "I"), (2, "Love"), (3, "You"), (4, "Chiu"), (5, "Chiu")]

    :rtype: list
    '''
    result = []
    # dem=0
    # for i in input_data:
    #     dem+=1
    #     print(dem,i)
    for i in enumerate(data, start=1):
        result.append(i)

    return result

def main():
    # xử lí in ra theo yêu cầu đề bài bên dưới
    result = solve(data)
    

if __name__ == "__main__":
    main()
