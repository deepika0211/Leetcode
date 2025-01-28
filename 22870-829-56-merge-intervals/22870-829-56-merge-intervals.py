class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval:interval[0])
        merg=[]
        for i in intervals:
            if not merg or merg[-1][1]<i[0]:
                merg.append(i)
            else:
                merg[-1]=[merg[-1][0], max(merg[-1][1], i[1])]
        return merg
        