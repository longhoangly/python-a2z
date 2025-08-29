"""
1️⃣ Sum all numbers in string → "abc12xyz34poq567" → Output: 613
613 = 12 + 34 + 567 / no special characters

2️⃣ Reverse string but preserve space positions
"My name is California" -> "ainrofilaC si eman yM" (reversed) → "ai nrof il aCsiemanyM" (reversed + keep position of spaces)
"""


def sum_all_numbers_in_string(input_str):
    import re

    pattern = re.compile(r"\d+")
    numbers = pattern.findall(input_str)
    sumary = sum([int(val) for val in numbers])
    print(sumary)


def remove_all_numbers_in_string(input_str):
    import re

    pattern = re.compile(r"\d+")
    numbers = pattern.findall(input_str)
    for num in numbers:
        input_str = input_str.replace(num, "")
    print(input_str)


def reversed_keep_space_position(input_str):
    chars = list(input_str)
    print(chars)

    space_indexs = []
    for i, char in enumerate(chars):
        if char == " ":
            space_indexs.append(i)
    print(space_indexs)

    chars.reverse()
    print(chars)

    chars_only = [char for char in chars if char != " "]
    print(chars_only)

    for index in space_indexs:
        chars_only.insert(index, " ")
    print(chars_only)

    print("".join(chars_only))


if __name__ == "__main__":
    sum_all_numbers_in_string("abc12xyz34poq567")
    sum_all_numbers_in_string("ab&%(%)^_++_\"\":c12xyz34poq567")

    remove_all_numbers_in_string("abc12xyz34poq567")
    remove_all_numbers_in_string("ab&%(%)^_++_\"\":c12xyz34poq567")

    reversed_keep_space_position("My name is California")
