#!/usr/bin/env python3


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


def your_function(text):
    '''Trả về Counter object chứa tần xuất xuất hiện của các từ trong `text`
    :rtype Counter
    '''
    # Sửa tên và function cho phù hợp, trả về kết quả yêu cầu.
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    raise NotImplementedError(
        "Học viên chưa thực hiện tìm số lần xuất hiện của từng từ"
    )

    return result


def your_function_2(top_n, counter):
    '''Trả về list chứa các tuple của top_n từ xuất hiện nhiều nhất kèm
    số lần xuất hiện của từ đó

    :rtype list:
    '''
    # Sửa tên function cho phù hợp, trả về kết quả yêu cầu.
    result = None

    # Xoá dòng sau và viết code vào đây set các giá trị phù hợp
    raise NotImplementedError(
        "Học viên chưa tìm 3 từ xuất hiện nhiều nhất"
    )

    return result


def solve(input_data):
    '''Học viên không cần viết code trong hàm `solve`, chỉ thực hiện
    đổi tên lại function của mình cho phù hợp

    :rtype list:
    '''
    result = your_function_2(3, your_function(input_data))

    return result


def main():
    text = data
    print(solve(text))


if __name__ == "__main__":
    main()
