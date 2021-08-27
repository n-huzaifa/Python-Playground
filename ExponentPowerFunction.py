def power(num, exponent):
    result = 1
    for i in range(exponent):
        result = result * num
    return result


print(power(2, 2))
