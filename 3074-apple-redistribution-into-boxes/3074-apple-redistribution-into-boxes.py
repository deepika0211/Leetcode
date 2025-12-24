class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        ans=0
        capacity.sort(reverse=True)
        total = sum(apple)
        for i in capacity:
            if total > 0:
                ans+=1
                total = total -i
            elif total <=0:
                break
        return ans
            