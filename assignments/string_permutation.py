
def permutation(string, left, right):
    if left == right:
        print(''.join(string))
    else:
        for i in range(left, right):
            string[left], string[i] = string[i], string[left]
            permutation(string, left+1, right)
            string[left], string[i] = string[i], string[left]


string = 'abc'
permutation(list(string), 0, len(string))
