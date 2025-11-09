class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        both = zip(heights,names)
        ans=sorted(both,reverse=True)
        return [name for i, name in ans]