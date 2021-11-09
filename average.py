import calculator


def average(arr):
    total = 0
    count = 0
    for i in arr:
        count = calculator.add(count, 1)
        total = calculator.add(total, i)

    return calculator.divide(total/count)
