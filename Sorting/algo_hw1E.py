# Task 1 (A from Codeforces: https://codeforces.com/group/dAhOSPf3oD/contest/349149/problem/A)
import sys


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        q = arr[randint(0, len(arr) - 1)]
        lower = []
        equal = []
        bigger = []
        for elem in arr:
            if elem < q:
                lower.append(elem)
            elif elem == q:
                equal.append(elem)
            else:
                bigger.append(elem)
        return quicksort(lower) + equal + quicksort(bigger)


def main():
    a = sys.stdin.read().split()
    n = int(a[0])
    arr = list(map(int, a[1:]))
    print(" ".join(map(str, quicksort(arr))))  # print(str(*quicksort(arr)))


if __name__ == "__main__":
    main()


# Task 2 (B from Codeforces: https://codeforces.com/group/dAhOSPf3oD/contest/349149/problem/B)
import sys


def count_sort(arr):
    counts = [0] * 101
    result = []
    for elem in arr:
        counts[elem] += 1

    for index, c in enumerate(counts):
        if c == 0:
            continue
        elif c == 1:
            result.append(index)
        else:
            b = [index for _ in range(1, c + 1)]
            result += b

    return result


def main():
    a = sys.stdin.read().split()
    n = int(a[0])
    arr = list(map(int, a[1:]))
    print(" ".join(map(str, count_sort(arr))))


if __name__ == "__main__":
    main()

# n = int(input())
# arr = [randint(0,100) for x in range(n)]
# print(*arr)
# print(" ".join(map(str, count_sort(arr))))


# Task 3 (sort colors from Leetcode: https://leetcode.com/problems/sort-colors/)
from random import randint
import sys


def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def main():
    a = sys.stdin.read().split()
    arr = list(map(int, a))
    print(" ".join(map(str, bubble_sort(arr))))


if __name__ == "__main__":
    main()

# n = int(input())
# arr = [randint(0, 2) for x in range(n)]
# print(*arr)
# print(" ".join(map(str, bubble_sort(arr))))

# стоит использовать Dutch_National_Flag
