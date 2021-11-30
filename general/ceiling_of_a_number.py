def ceiling_of_a_number(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end: 
        mid = (start + end) // 2
        if arr[mid] == target: 
            return arr[mid]
        elif arr[mid] < target:
            start = mid + 1
        else: 
            end = mid - 1
    return arr[start]

def main():
    arr = [2,3,5, 9, 14, 16, 18 ]
    target = 13
    print(ceiling_of_a_number(arr, target))

main()