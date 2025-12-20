class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete = 0
        for col in zip(*strs):
            if list(col) != sorted(col):
                delete += 1
        return delete
        

        