class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        bro = set(brokenLetters)
        return sum(not set(w) & bro for w in text.split())
        