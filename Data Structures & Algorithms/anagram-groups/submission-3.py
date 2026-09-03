class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            results[sorted_word].append(word)

        return list(results.values())
        