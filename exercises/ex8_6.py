#!/usr/bin/env python3


import re
import collections


__doc__ = '''
Kiểu dữ liệu collections.Counter giúp cho việc đếm trờ nên rất dễ dàng.
https://docs.python.org/3/library/collections.html#collections.Counter

Cho đoạn văn bản `s` như bên dưới

Yêu cầu:
- Tìm tần suất xuất hiện của mỗi từ
- Tìm 3 từ xuất hiện nhiều nhất, cùng số lần xuất hiện.
'''


data = (
    'A Counter is a dict subclass for counting hashable objects. It is an '
    'unordered collection where elements are stored as dictionary keys and '
    'their counts are stored as dictionary values. Counts are allowed to be '
    'any integer value including zero or negative counts. The Counter class '
    'is similar to bags or multisets in other languages.'
)


def func_counter(text):
    '''Trả về Counter object chứa tần xuất xuất hiện của các từ trong `text`
    :rtype Counter
    '''
    result = collections.Counter()

    words = re.findall(r'\w+', data.lower())
    for word in words:
        result[word] += 1
    return result


def top_word(top_n, counter):
    '''Trả về list chứa các tuple của top_n từ xuất hiện nhiều nhất kèm
    số lần xuất hiện của từ đó

    :rtype list:
    '''
    result = list(counter.items())

    return result


def top_word_2(top_n, data):
    words = re.findall(r'\w+', data.lower())
    result = collections.Counter(words).most_common(top_n)
    return result


def solve(input_data):
    '''Học viên không cần viết code trong hàm `solve`, chỉ thực hiện
    đổi tên lại function của mình cho phù hợp

    :rtype list:
    '''
    result = top_word(3, func_counter(input_data))
    # result = top_word_2(3, input_data)
    return result


def main():
    text = data
    print(solve(text))


if __name__ == "__main__":
    main()
