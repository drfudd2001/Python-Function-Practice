# Write a Python function called max_num()to find the maximum of three numbers.
# Write a Python function called mult_list() to multiply all the numbers in a list.
# Write a Python function called rev_string() to reverse a string.

# Write a Python function called num_within() to check whether a number falls in
# a given range. The function accepts the number, beginning of range, and end of
# range (inclusive) as arguments.
#   Examples: num_within( 3,2,4) returns True,
#             num_within( 3,1,3) returns True,
#             num_within(10,2,5) returns False.

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.


def max_num(i, j, k):
    return max(i, j, k)


def mult_list(nums):
    product = 1
    for i in nums:
        product *= i
    return product


def rev_string(text):
    return text[::-1]


def num_within(i, j, k):
    return (j <= i and i <= k)


def pascal(n):
    print()
    Triangle = []
    for row in range(n):
        Triangle.append([])
        for col in range(row+1):
            if (col == 0 or col == row):
                Triangle[row].append(1)
            else:
                Triangle[row].append(
                    Triangle[row-1][col-1]+Triangle[row-1][col])
        print(*Triangle[row])
    return


# Call each function
print(max_num(5, 3, 12))
print(mult_list([1, 4, 7, 2]))
print(rev_string("Hello World!"))
print(num_within(3, 2, 4))
print(num_within(3, 1, 3))
print(num_within(10, 2, 5))
pascal(1)
pascal(5)