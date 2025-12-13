class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        list1 = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }
        valid=[]
        for i in range(len(code)):
            if not isActive[i]:
                continue
            if businessLine[i] not in list1:
                continue
            if not code[i]:
                continue
            if not all(c.isalnum() or c=='_' for c in code[i]):
                continue
            valid.append((list1[businessLine[i]],code[i]))
        valid.sort()
        return [c for _, c in valid]

        