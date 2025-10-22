import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        l1 = heapq.heapify(nums1)
        l2 = heapq.heapify(nums2)
        while len(nums1) != 0 and len(nums2) !=0 :
            temp1 = heapq.heappop(nums1)
            temp2 = heapq.heappop(nums2)
            if temp1 < temp2:
                heapq.heappush(nums2, temp2)
                for i in heapq.nsmallest(len(nums2), nums2):
                    result.append([temp1, i])
            else:
                heapq.heappush(nums1, temp1)
                for i in heapq.nsmallest(len(nums1), nums1):
                    result.append([i, temp2])


        #print(result[:k])
        return result[:k]
    def kSmallestPairs1(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        result = []
        visit = set()
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                   result.append([nums1[i], nums2[j]])
        result2 = sorted(result, key=lambda x :x[0] + x[1])
        #print(result2)
        return result2[:k]

    