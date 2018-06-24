#!/usr/bin/env python3


def solve(text):
    '''Thực hiện biến đổi

      input: [a, abbbccccdddd, xxyyyxyyx]
      output: [a, abb3cc4dd4, xx2yy3xyy2x]

    Giải thích: Những chữ cái không lặp lại thì output giữ nguyên chữ cái đó.
    Những chữ cái liên tiếp sẽ in ra 2 lần + số lần lặp lại liên tiếp.

    Đây là một biến thể của một thuật toán nén dữ liệu có tên Run-length
    encoding (RLE).
    '''
    result = ''
    numb = 1
    sub_str = ''
    temp = text[0]
    flag = True
    for element in text:
        if flag is True:
            flag = False
            sub_str = element[0]
        elif element == temp:
            numb = numb + 1
        else:
            sub_str = (temp*2 + str(numb)) if (numb != 1) else temp
            result = result + sub_str
            temp = element
            numb = 1
    sub_str = (temp*2 + str(numb)) if (numb != 1) else temp
    result = result + sub_str
    return result


def main():
    print(solve('abbbccccdddd'))


if __name__ == "__main__":
    main()
