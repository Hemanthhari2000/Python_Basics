
# ======================= Problem =======================

'''

Given two binary strings a and b, return their sum as a binary string.


'''

# ======================= Test Case =======================
'''

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.


'''

# ======================= Solution =======================


def addBinary(a, b):

    x = list(a)
    y = list(b)
    x = [int(i) for i in x][::-1]
    y = [int(i) for i in y][::-1]

    i, j = 0, 0
    rs = []
    carry = 0
    while i < len(x) or j < len(y):

        runningSum = carry

        if (i < len(x)):
            runningSum += x[i]
            i += 1
        if (j < len(y)):
            runningSum += y[j]
            j += 1

        if runningSum > 1:
            carry = 1
            runningSum = 0 if runningSum % 2 == 0 else 1
        else:
            carry = 0

        rs.append(runningSum)

    if carry:
        rs.append(carry)
    return rs[::-1]


result = addBinary("1010", "1011")
result = [str(i) for i in result]
result = ''.join(result)
print(result)
