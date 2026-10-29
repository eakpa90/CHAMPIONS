def move_zeros(numbers):
    non_zeros = [num for num in numbers if num != 0]

    zero_count = numbers.count(0)

    return non_zeros + [0] * zero_count

