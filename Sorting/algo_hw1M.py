# Task 1 (https://codeforces.com/group/dAhOSPf3oD/contest/349149/problem/C)
import sys

pair_counter = 0


def mod_merge(arr, l, m, r):
    global pair_counter
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(n1):
        L[i] = arr[l + i]

    for j in range(n2):
        R[j] = arr[m + 1 + j]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            pair_counter += n1 - i  # len(L)
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def modified_merge_sort(arr, l, r):
    global pair_counter
    if l < r:
        m = l + (r - l) // 2
        modified_merge_sort(arr, l, m)
        modified_merge_sort(arr, m + 1, r)
        mod_merge(arr, l, m, r)
    return pair_counter


def main():
    a = sys.stdin.read().split()
    n = int(a[0])
    arr = list(map(int, a[1:]))
    print(modified_merge_sort(arr, l=0, r=len(arr) - 1))


if __name__ == "__main__":
    main()

# from random import randint
#
# N = 10
# array = [randint(0, 10) for _ in range(N)]
# print(array)
# print(modified_merge_sort(array, l=0, r=len(array) - 1))


# вначале чтобы обновить счетчик
# def merge_sort_with_inversions(arr):
#     global pair_counter
#     pair_counter = 0  # Обнуляем счётчик один раз для всего массива
#     modified_merge_sort(arr, 0, len(arr) - 1)
#     return pair_counter


# Task 2 (from Leetcode: https://leetcode.com/problems/wiggle-sort-ii/)
class Solution(object):
    def count_sort(self, arr):
        counts = [0] * (max(arr) + 1)
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

    def wiggleSort(self, nums):
        array = self.count_sort(nums)  # sort our array in ascending order
        len_arr = len(nums)
        medium_el = (len_arr - 1) // 2
        wiggle_array = []
        if len_arr % 2 == 0:
            for i in range(len_arr):
                if i <= medium_el:
                    wiggle_array.append(array[medium_el - i])
                    wiggle_array.append(array[len_arr - 1 - i])
        else:
            for i in range(len_arr):
                if i < medium_el:
                    wiggle_array.append(array[medium_el - i])
                    wiggle_array.append(array[len_arr - 1 - i])
            wiggle_array.append(array[0])
        nums[:] = wiggle_array
        print(nums)


# Task 3 (from Codeforces: https://codeforces.com/problemset/problem/1713/B)
import sys


def get_nul_optimal(arr):
    new_arr = []
    new_arr.append(arr[0])
    # check if we have the same elements next to each other
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            new_arr.append(arr[i])
    # if the small element is between large elements, it will take more operations than it's not
    for i in range(1, len(new_arr) - 1):
        if new_arr[i - 1] > new_arr[i] and new_arr[i] < new_arr[i + 1]:
            return "NO"
    return "YES"


def main():
    # a = list(map(int, input().split()))
    a = list(map(int, sys.stdin.read().split()))
    t = a[0]
    p = 1
    for i in range(t):
        array = list(map(int, a[p + 1 : p + 1 + a[p]]))
        print(get_nul_optimal(array))
        p = p + 1 + a[p]


if __name__ == "__main__":
    main()


# Task 4 (from Leetcode: https://leetcode.com/problems/top-k-frequent-elements/)
class Solution:
    def topKFrequent(self, nums: list[int], k: int):
        counts_plus = [0] * 10001
        counts_minus = [0] * 10000
        for i in range(len(nums)):
            if nums[i] >= 0:
                counts_plus[nums[i]] += 1
            else:
                counts_minus[(-1) * nums[i]] += 1

        most_frequent_elements = []
        for j in range(k):
            # m_freq_number_plus =
            # m_freq_number_minus =
            if max(counts_plus) >= max(counts_minus):
                m_freq_number = counts_plus.index(max(counts_plus))
                counts_plus[m_freq_number] = 0
                most_frequent_elements.append(m_freq_number)
            else:
                m_freq_number = counts_minus.index(max(counts_minus))
                counts_minus[m_freq_number] = 0
                most_frequent_elements.append((-1) * m_freq_number)
        return most_frequent_elements


# Task 5 (from Leetcode:https://leetcode.com/problems/kth-largest-element-in-an-array/)
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        counts = [0] * (2 * 10**4 + 1)
        for i in nums:
            counts[i] += 1
        asc_arr = []
        for i in range(-10000, 0, 1):
            for j in range(counts[i]):
                asc_arr.append(i)
        for i in range(0, 10001):
            for j in range(counts[i]):
                asc_arr.append(i)
        print(asc_arr)
        return asc_arr[len(asc_arr) - k]


# версия с quick sort характером
from random import randint


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        pivot = nums[randint(0, len(nums) - 1)]
        high = [x for x in nums if x > pivot]
        equal = [x for x in nums if x == pivot]
        low = [x for x in nums if x < pivot]

        if len(high) >= k:
            return self.findKthLargest(high, k)
        elif len(high) + len(equal) >= k:
            return pivot
        else:
            return self.findKthLargest(low, k - len(high) - len(equal))
