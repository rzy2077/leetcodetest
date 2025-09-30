from typing import List
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        result = []
        lenSpell = len(spells)
        potions.sort()
        l1 = len(potions)
        for spell in spells:
            left = 0
            right = l1 - 1
            index = -1
            while left < right:
                mid = (right - left)//2 + left
                if spell * potions[mid] >= success:
                    index = mid
                    right = mid - 1
                else:
                    left = mid + 1
            print(f'index {index}')
            result.append(index)
        return result



if __name__ == '__main__':

    s1 = Solution()

    s1.successfulPairs()