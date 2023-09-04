class Solution:
    def convert_to_str(self, letters: List[str]) -> str:
        word = ""
        for letter in letters:
            word += letter
        return word

    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return self.convert_to_str(word1) == self.convert_to_str(word2)