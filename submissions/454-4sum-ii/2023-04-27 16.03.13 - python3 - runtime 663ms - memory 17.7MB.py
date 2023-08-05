from collections import Counter

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res = 0
        two_sums_1 = []
        for n1 in nums1:
            for n2 in nums2:
                two_sums_1.append(n1 + n2)
        two_sums_1 = Counter(two_sums_1)
        two_sums_1 = sorted(two_sums_1.items(), key=lambda x: x[0])
        
        two_sums_2 = []
        for n3 in nums3:
            for n4 in nums4:
                two_sums_2.append(n3 + n4)
        two_sums_2 = Counter(two_sums_2)
        two_sums_2 = sorted(two_sums_2.items(), key=lambda x: x[0])

        res = 0
        ptr1, ptr2 = 0, len(two_sums_2) -1
        while ptr1 < len(two_sums_1) and ptr2 > -1:
            if two_sums_1[ptr1][0] + two_sums_2[ptr2][0] > 0:
                ptr2 -= 1
            elif two_sums_1[ptr1][0] + two_sums_2[ptr2][0] < 0:
                ptr1 += 1
            else:
                res += two_sums_1[ptr1][1] * two_sums_2[ptr2][1]
                ptr2 -= 1
                ptr1 += 1
        return res