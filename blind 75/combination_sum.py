class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # backtracking with dfs
        length = len(candidates)
        result = []

        def dfs(index, currentList, total):
            # base case
            if total == target:
                result.append(currentList.copy())
                return
            if total > target or index >= length:
                return

            # else
            currentList.append(candidates[index])
            dfs(index, currentList, total + candidates[index])
            # pop when reached the end of dfs for first recursion
            currentList.pop()
            dfs(index + 1, currentList, total)

        dfs(0, [], 0)

        return result
