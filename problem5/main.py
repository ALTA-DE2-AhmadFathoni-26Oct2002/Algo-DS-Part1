def max_sequence(arr):
    n = len(arr)
    max_sum = 0

    for x in range (n):
        window_sum = 0
        for y in range (x, n):
            window_sum += arr[y]
            max_sum = max(window_sum, max_sum)
        
    return max_sum

if __name__ == "__main__":
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_sequence([-2, -5, 6, -2, -3, 1, 5, -6]))    # 7
    print(max_sequence([-2, -3, 4, -1, -2, 1, 5, -3]))    # 7
    print(max_sequence([-2, -5, 6, -2, -3, 1, 6, -6]))    # 8
    print(max_sequence([-2, -5, 6, 2, -3, 1, 6, -6]))     # 12