class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        first_k = []
        i = 0
        sorted_freq_map = dict(sorted(freq_map.items(), key=lambda item: item[1], reverse=True))
        # print(sorted_freq_map)
        sorted_freq_keys = list(sorted_freq_map.keys())
        while k > 0:
            first_k.append(sorted_freq_keys[i])
            k -= 1
            i += 1
        
        return first_k


            
