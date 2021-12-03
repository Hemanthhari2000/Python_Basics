def main():
    arr = [1, 5, 3, 2, 2]
    target = 2

    result = [i for i, j in enumerate(sorted(arr)) if j == target]
    print(result)


main()
 