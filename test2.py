from  collections import defaultdict
class solution:
    def rotateString(self, s: str, goal: str) -> bool:
        l1 = len(s)
        l2 = len(goal)
        if l1 != l2:
            return  False

        for i in range(l2):

            if (s[i:] + s[:i] ) == goal:
                return True
        return  False




if __name__ == '__main__':
        s1 = str(input())
        target = str(input())
        solution = solution()
        print(solution.rotateString(s1, target))
