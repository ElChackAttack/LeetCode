class Solution:
    # 1) Sorted solution
    # For this problem if we sort the List then it becomes a lot easier
    def sorted_solution(self, strs: List[str]) -> str:
        strs = sorted(strs, key=len)
        num_words = len(strs)
        if num_words == 0:
            return ""
        print(strs)
        solution = ""
        for ptr in range(len(strs[0])):
            letter = strs[0][ptr]
            for word in strs[1::]:
                if word[ptr] != letter:
                    return solution
            solution += letter
        return solution
    # 2) Unsorted solution

    def unsorted_solution(self, strs: List[str]) -> str:
        num_words = len(strs)
        if num_words == 0:
            return ""
        print(strs)
        solution = ""
        shortest_word_length = self.find_shortest_word_length(strs)
        for ptr in range(shortest_word_length):
            letter = strs[0][ptr]
            for word in strs[1::]:
                if word[ptr] != letter:
                    return solution
            solution += letter
        return solution
    # The problem is mostly the same just gotta make a helper function to find shortest word length

    def find_shortest_word_length(self, strs: List[str]) -> int:
        word_length = len(strs[0])
        for word in strs[1::]:
            current_word_length = len(word)
            if len(word) < word_length:
                word_length = current_word_length
        return word_length

    def longestCommonPrefix(self, strs: List[str]) -> str:

        # return self.sorted_solution(strs)
        return self.unsorted_solution(strs)
