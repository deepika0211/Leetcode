class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        largest = -1
        for i in range(len(arr)-1,-1,-1):
            if arr[i]>largest:
                res.append(largest)
                largest=arr[i]
            else:
                res.append(largest)
        return res[::-1]
        