class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        both={}
        for i in range(len(names)):
            both[heights[i]]=names[i]
        sorted_heights = sorted(heights, reverse=True)
        return [both[h] for h in sorted_heights]