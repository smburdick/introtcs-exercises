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

def list_to_int(n):
    res = 0
    for i in range(len(n)):
        res = res + n[i] * (10** (len(n) - i - 1))
    return res

def sum_lists(a, b):
    return int_to_list(list_to_int(a) + list_to_int(b))

def karatsuba_multiply(x, y):
    """
    Defined same way as gradeschool_multiply but using Karatsuba's algorithm
    """
    if min(len(x), len(y)) < 3: return gradeschool_multiply(x, y)
    n = max(len(x), len(y))
    # pad with zeroes if needed
    xs = [0] * (n - len(x)) + x; ys = [0] * (n - len(y)) + y
    m = n // 2
    xstop = xs[:-m]; xsbot = xs[-m:]
    ystop = ys[:-m]; ysbot = ys[-m:]
    return int_to_list((10**(2*m) - 10**m) * list_to_int(karatsuba_multiply(xstop, ystop)) + (10**m) \
     * list_to_int(karatsuba_multiply(sum_lists(xstop, xsbot), sum_lists(ystop, ysbot))) \
     + (1 - 10**m) * list_to_int(karatsuba_multiply(xstop, ystop)))

## testing
print(sum_lists([5,5,5],[4,5,6]))
print(list_to_int([1,2,3,4,5]))
print(list_to_int([2,0,4]))
print(int_to_list(123 * 456) == gradeschool_multiply([1,2,3], [4,5,6]))
print(1234 * 5678)
print(karatsuba_multiply([1,2,3, 4], [5, 6, 7, 8]))
print(int_to_list(1234 * 5678) == karatsuba_multiply([1,2,3, 4], [5, 6, 7, 8]))
