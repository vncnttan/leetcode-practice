class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        counter = 0

        bannedWords = set(w for w in bannedWords)

        for w in message:
            if w in bannedWords:
                counter += 1
                if counter >= 2:
                    return True
        
        return False 