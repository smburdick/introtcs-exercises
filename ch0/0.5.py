def gradeschool_multiply(x, y):
    """
    x, y are lists of integers representing the digits of
    two integers to be multiplied together
    @return the digits of x * y expressed as a list
    """
    result = 0
    for i in range(len(x)):
        for j in range(len(y)):
            result = result + 10 ** (i + j) * x[len(x) - i - 1] * y[len(x) - j - 1]
    return int_to_list(result)

def int_to_list(n):
    result = str(n)
    # make result into a list
    return [int(result[i]) for i in range(len(result))]

def karatsuba_multiply(x, y):
    """
    Defined same way as gradeschool_multiply
    """
    return [] # TODO

## testing
print(int_to_list(123 * 456) == gradeschool_multiply([1,2,3], [4,5,6]))
